#!/usr/bin/env python3
"""Convert the DTDL ISA-95 source model to an editable RDF/XML ontology."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import quote
from xml.etree import ElementTree as ET
from xml.dom import minidom


SOURCE_ROOT = Path(__file__).parents[1] / "ontology" / "isa95" / "source" / "ISA95"
OUTPUT_FILE = Path(__file__).parents[1] / "generated" / "isa95.rdf"

RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
RDFS = "http://www.w3.org/2000/01/rdf-schema#"
OWL = "http://www.w3.org/2002/07/owl#"
XSD = "http://www.w3.org/2001/XMLSchema#"
DCTERMS = "http://purl.org/dc/terms/"
ISA95 = "https://schema.trumpf.com/testing/isa95/"

NS = {"rdf": RDF, "rdfs": RDFS, "owl": OWL, "xsd": XSD, "dcterms": DCTERMS}
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)
ET.register_namespace("isa95", ISA95)


def local_name(value: str) -> str:
    """Create a stable RDF local name from a DTMI or member name."""
    if value.startswith("dtmi:"):
        value = value[5:]
    value = value.replace(":", "_").replace(";", "_v")
    value = re.sub(r"[^A-Za-z0-9_.-]", "_", value)
    return value.strip("_") or "unnamed"


def resource_uri(dtmi: str) -> str:
    return ISA95 + local_name(dtmi)


def source_files() -> list[Path]:
    return sorted(SOURCE_ROOT.rglob("*.json"))


def read_interfaces() -> list[dict[str, Any]]:
    return [json.loads(path.read_text(encoding="utf-8")) for path in source_files()]


def add_literal(parent: ET.Element, predicate: str, value: Any) -> None:
    separator = "#" if "#" in predicate else "/"
    namespace, local = predicate.rsplit(separator, 1)
    element = ET.SubElement(parent, f"{{{namespace}{separator}}}{local}")
    element.text = str(value)


def add_annotation(parent: ET.Element, predicate: str, value: Any) -> None:
    if value is not None:
        add_literal(parent, predicate, value)


def property_range(schema: Any) -> str:
    if isinstance(schema, str) and schema.startswith("dtmi:"):
        return resource_uri(schema)
    if isinstance(schema, dict):
        schema_type = schema.get("@type")
        if schema_type == "Map":
            return XSD + "string"
        if schema_type:
            return XSD + "string"
    return {
        "string": XSD + "string",
        "integer": XSD + "integer",
        "double": XSD + "double",
        "dateTime": XSD + "dateTime",
        "Enum": XSD + "string",
    }.get(schema, XSD + "string")


def add_property_metadata(
    element: ET.Element,
    content: dict[str, Any],
    original_id: str,
    label: str,
) -> None:
    add_annotation(element, RDFS + "label", label)
    add_annotation(element, RDFS + "comment", content.get("description"))
    add_annotation(element, ISA95 + "sourceComment", content.get("comment"))
    add_annotation(element, ISA95 + "sourceDtmi", original_id)


def convert() -> None:
    interfaces = read_interfaces()
    datatype_label_counts = Counter(
        content.get("displayName") or content.get("name")
        for interface in interfaces
        for content in interface.get("contents", [])
        if content.get("name") and content.get("@type") == "Property"
    )
    shared_object_properties: dict[str, list[tuple[dict[str, Any], dict[str, Any]]]] = {}
    for interface in interfaces:
        for content in interface.get("contents", []):
            name = content.get("name")
            if not name or content.get("@type") == "Property":
                continue
            label = content.get("displayName") or name
            shared_object_properties.setdefault(label, []).append((interface, content))

    root = ET.Element(f"{{{RDF}}}RDF")
    ontology = ET.SubElement(root, f"{{{OWL}}}Ontology", {f"{{{RDF}}}about": ISA95})
    add_annotation(ontology, RDFS + "label", "ISA-95 ontology converted from DTDL")
    add_annotation(ontology, DCTERMS + "title", "ISA-95 reference ontology")
    add_annotation(ontology, DCTERMS + "source", "ontology/isa95/source/ISA95")
    add_annotation(ontology, OWL + "versionInfo", "Generated from DTDL source")

    for interface in interfaces:
        original_id = interface["@id"]
        class_element = ET.SubElement(
            root,
            f"{{{OWL}}}Class",
            {f"{{{RDF}}}about": resource_uri(original_id)},
        )
        add_annotation(class_element, RDFS + "label", interface.get("displayName"))
        add_annotation(class_element, RDFS + "comment", interface.get("description"))
        add_annotation(class_element, ISA95 + "sourceComment", interface.get("comment"))
        add_annotation(class_element, ISA95 + "sourceDtmi", original_id)
        for parent in interface.get("extends", []):
            ET.SubElement(
                class_element,
                f"{{{RDFS}}}subClassOf",
                {f"{{{RDF}}}resource": resource_uri(parent)},
            )

    for label, members in sorted(shared_object_properties.items()):
        property_uri = ISA95 + "object-property/" + quote(label, safe="")
        element = ET.SubElement(
            root,
            f"{{{OWL}}}ObjectProperty",
            {f"{{{RDF}}}about": property_uri},
        )
        add_annotation(element, RDFS + "label", label)
        for interface, content in members:
            add_annotation(element, RDFS + "comment", content.get("description"))
            add_annotation(
                element,
                ISA95 + "sourceDtmi",
                f"{interface['@id']}#{content['name']}",
            )
            add_annotation(element, ISA95 + "dtdlType", content.get("@type"))

    for interface in interfaces:
        owner_uri = resource_uri(interface["@id"])
        owner_name = local_name(interface["@id"])
        for content in interface.get("contents", []):
            name = content.get("name")
            if not name or content.get("@type") != "Property":
                continue
            label = content.get("displayName") or name
            if datatype_label_counts[label] > 1:
                owner_label = interface.get("displayName") or interface["@id"]
                owner_id = interface["@id"]
                label = f"{label} ({owner_label} [{owner_id}]: {name})"
            property_uri = ISA95 + owner_name + "__" + local_name(name)
            if content["@type"] == "Property":
                element = ET.SubElement(
                    root,
                    f"{{{OWL}}}DatatypeProperty",
                    {f"{{{RDF}}}about": property_uri},
                )
                ET.SubElement(element, f"{{{RDFS}}}domain", {f"{{{RDF}}}resource": owner_uri})
                ET.SubElement(element, f"{{{RDFS}}}range", {f"{{{RDF}}}resource": property_range(content.get("schema"))})
            add_property_metadata(element, content, f"{interface['@id']}#{name}", label)
            add_annotation(element, ISA95 + "dtdlType", content.get("@type"))
            add_annotation(element, ISA95 + "writable", content.get("writable"))

    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    pretty = minidom.parseString(raw).toprettyxml(indent="  ", encoding="utf-8")
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(pretty)
    print(f"Wrote {OUTPUT_FILE} from {len(interfaces)} DTDL interfaces")


if __name__ == "__main__":
    convert()