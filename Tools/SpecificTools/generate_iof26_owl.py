#!/usr/bin/env python3
"""Gather locally released IOF ontologies into one RDF/XML OWL file."""

from __future__ import annotations

import copy
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
from xml.dom import minidom
from xml.etree import ElementTree as ET


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "ontology" / "iof26" / "source" / "ontology-master"
OUTPUT_FILE = REPOSITORY_ROOT / "generated" / "iof26.owl"
ONTOLOGY_IRI = "https://schema.trumpf.com/testing/iof26/"

RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
RDFS = "http://www.w3.org/2000/01/rdf-schema#"
OWL = "http://www.w3.org/2002/07/owl#"
DCTERMS = "http://purl.org/dc/terms/"
XML = "http://www.w3.org/XML/1998/namespace"

ENTRYPOINTS = (
    "core/AboutIOFProd.rdf",
    "maintenance/AboutIOFProd.rdf",
    "supplychain/AboutIOFProd.rdf",
    "certification/AboutIOFProd.rdf",
    "productionplanning/ProductionPlanning.rdf",
)


def source_documents() -> list[Path]:
    return sorted(SOURCE_ROOT.rglob("*.rdf"))


def parse_document(path: Path) -> ET.Element:
    return ET.parse(path).getroot()


def document_base(path: Path, root: ET.Element) -> str:
    return urljoin(path.resolve().as_uri(), root.get(f"{{{XML}}}base", ""))


def ontology_index(files: list[Path]) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = {}
    for path in files:
        root = parse_document(path)
        base = document_base(path, root)
        for ontology in root.findall(f"{{{OWL}}}Ontology"):
            about = ontology.get(f"{{{RDF}}}about")
            if about:
                iri = urljoin(base, about)
                index.setdefault(iri, []).append(path)
    return index


def catalog_targets(files: list[Path]) -> dict[str, list[Path]]:
    targets: dict[str, list[Path]] = {}
    catalog_ns = "urn:oasis:names:tc:entity:xmlns:xml:catalog"
    for catalog in sorted(SOURCE_ROOT.rglob("catalog-v001.xml")):
        root = ET.parse(catalog).getroot()
        for entry in root.findall(f"{{{catalog_ns}}}uri"):
            name = entry.get("name")
            location = entry.get("uri")
            if not name or not location:
                continue
            parsed = urlparse(location)
            if parsed.scheme == "file":
                if parsed.netloc not in ("", "localhost"):
                    continue
                candidate = Path(unquote(parsed.path))
            elif parsed.scheme:
                continue
            else:
                candidate = (catalog.parent / unquote(location)).resolve()
            if candidate.is_file():
                targets.setdefault(name, []).append(candidate)
    return targets


def direct_source_path(iri: str) -> Path | None:
    parsed = urlparse(iri)
    prefix = "/ontology/"
    if parsed.netloc != "spec.industrialontologies.org" or not parsed.path.startswith(prefix):
        return None
    relative = unquote(parsed.path[len(prefix):]).lstrip("/")
    candidates = [SOURCE_ROOT / relative]
    trimmed = relative.rstrip("/")
    if trimmed:
        candidates.extend((SOURCE_ROOT / f"{trimmed}.rdf", SOURCE_ROOT / trimmed / "AboutIOFProd.rdf"))
    return next((path.resolve() for path in candidates if path.is_file()), None)


def resolve_import(
    iri: str,
    catalogs: dict[str, list[Path]],
    ontologies: dict[str, list[Path]],
) -> Path | None:
    for path in catalogs.get(iri, []):
        if path.is_file():
            return path.resolve()

    direct = direct_source_path(iri)
    if direct:
        return direct

    candidates = ontologies.get(iri, [])
    if not candidates:
        return None
    return min(
        candidates,
        key=lambda path: (
            any(part in {"test", "examples", "migration", "addenda"} for part in path.parts),
            len(path.parts),
            str(path),
        ),
    )


def import_closure() -> tuple[list[tuple[Path, ET.Element]], list[str]]:
    files = source_documents()
    catalogs = catalog_targets(files)
    ontologies = ontology_index(files)
    queue = [(SOURCE_ROOT / entry).resolve() for entry in ENTRYPOINTS]
    visited: dict[Path, ET.Element] = {}
    unresolved: set[str] = set()

    for entry in queue:
        if not entry.is_file():
            raise FileNotFoundError(f"IOF entrypoint not found: {entry}")

    while queue:
        path = queue.pop()
        if path in visited:
            continue
        root = parse_document(path)
        visited[path] = root
        base = document_base(path, root)
        for imported in root.iter(f"{{{OWL}}}imports"):
            resource = imported.get(f"{{{RDF}}}resource")
            if not resource:
                continue
            iri = urljoin(base, resource)
            target = resolve_import(iri, catalogs, ontologies)
            if target is None:
                unresolved.add(iri)
            else:
                queue.append(target)

    return sorted(visited.items()), sorted(unresolved)


def register_namespaces(files: list[Path]) -> None:
    for path in files:
        for _, (prefix, uri) in ET.iterparse(path, events=("start-ns",)):
            if prefix not in {"xml", "xmlns"}:
                try:
                    ET.register_namespace(prefix, uri)
                except ValueError:
                    pass
    for prefix, uri in (("rdf", RDF), ("rdfs", RDFS), ("owl", OWL), ("dcterms", DCTERMS)):
        ET.register_namespace(prefix, uri)


def remove_imports(element: ET.Element) -> None:
    for parent in element.iter():
        for child in list(parent):
            if child.tag == f"{{{OWL}}}imports":
                parent.remove(child)


def build_ontology(documents: list[tuple[Path, ET.Element]]) -> ET.Element:
    register_namespaces([path for path, _ in documents])
    root = ET.Element(f"{{{RDF}}}RDF")
    ontology = ET.SubElement(root, f"{{{OWL}}}Ontology", {f"{{{RDF}}}about": ONTOLOGY_IRI})
    ET.SubElement(ontology, f"{{{RDFS}}}label").text = "IOF ontology aggregate"
    ET.SubElement(ontology, f"{{{DCTERMS}}}title").text = "Industrial Ontology Foundry ontology aggregate"
    ET.SubElement(ontology, f"{{{DCTERMS}}}source").text = "ontology/iof26/source/ontology-master"
    ET.SubElement(ontology, f"{{{OWL}}}versionInfo").text = "Generated from bundled IOF released ontology sources"

    for path, source_root in documents:
        base = document_base(path, source_root)
        for source_element in source_root:
            element = copy.deepcopy(source_element)
            element_base = urljoin(base, element.get(f"{{{XML}}}base", ""))
            element.set(f"{{{XML}}}base", element_base)
            remove_imports(element)
            root.append(element)
    return root


def main() -> None:
    documents, unresolved = import_closure()
    if unresolved:
        imports = "\n".join(f"- {iri}" for iri in unresolved)
        raise RuntimeError(f"Unresolved IOF imports; refusing to generate an incomplete ontology:\n{imports}")

    root = build_ontology(documents)
    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(minidom.parseString(raw).toprettyxml(indent="  ", encoding="utf-8"))
    print(f"Wrote {OUTPUT_FILE} from {len(documents)} IOF source documents")


if __name__ == "__main__":
    main()