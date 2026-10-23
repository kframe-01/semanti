#!/usr/bin/env python3
"""Generate a reviewed BFO alignment layer for the generated ISA-95 ontology."""

from __future__ import annotations

import csv
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.dom import minidom


ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "generated" / "isa95.rdf"
BFO_SOURCE_FILE = ROOT / "ontology" / "bfo15" / "source" / "bfo.owl"
OUTPUT_FILE = ROOT / "generated" / "isa95-bfo-alignment.rdf"
REVIEW_FILE = ROOT / "generated" / "isa95-bfo-review.csv"

RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
RDFS = "http://www.w3.org/2000/01/rdf-schema#"
OWL = "http://www.w3.org/2002/07/owl#"
DCTERMS = "http://purl.org/dc/terms/"
ISA95 = "https://schema.trumpf.com/testing/isa95/"
BFO_ONTOLOGY = "http://purl.obolibrary.org/obo/bfo.owl"
BFO = "http://purl.obolibrary.org/obo/BFO_"
ALIGNMENT = "https://schema.trumpf.com/testing/isa95-bfo-alignment/"

NS = {"rdf": RDF, "rdfs": RDFS, "owl": OWL, "dcterms": DCTERMS}
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)
ET.register_namespace("isa95", ISA95)
ET.register_namespace("bfo", "http://purl.obolibrary.org/obo/")

# These are direct, reviewed mappings. Do not infer a BFO category from the
# generated ISA-95 class hierarchy: most classes inherit from a schema base.
DOCKINGS: dict[str, tuple[str, str]] = {
    "digitaltwins_isa95_Person_v1": (
        BFO + "0000040",
        "The term denotes a person, a material entity.",
    ),
    "digitaltwins_isa95_PhysicalAsset_v1": (
        BFO + "0000040",
        "The source definition explicitly describes a physical asset as a physical piece of equipment.",
    ),
    "digitaltwins_isa95_MaterialLot_v1": (
        BFO + "0000040",
        "A material lot is a bounded amount of physical material.",
    ),
    "digitaltwins_isa95_MaterialSublot_v1": (
        BFO + "0000040",
        "A material sublot is a subdivision of a material lot and remains physical material.",
    ),
    "digitaltwins_isa95_WorkMaster_v1": (
        BFO + "0000031",
        "A work master specifies reusable work instructions and is information content dependent on a carrier.",
    ),
    "digitaltwins_isa95_WorkDefinition_v1": (
        BFO + "0000031",
        "A work definition specifies work and is information content dependent on a carrier.",
    ),
    "digitaltwins_isa95_WorkDirective_v1": (
        BFO + "0000031",
        "A work directive specifies instructions for a unit of work and is information content dependent on a carrier.",
    ),
    "digitaltwins_isa95_TestSpecification_v1": (
        BFO + "0000031",
        "A test specification prescribes test criteria and is information content dependent on a carrier.",
    ),
    "digitaltwins_isa95_TestResult_v1": (
        BFO + "0000031",
        "A test result records measured results and evaluation information.",
    ),
    "digitaltwins_isa95_PropertyMeasurement_v1": (
        BFO + "0000031",
        "A property measurement records a measurement value as information.",
    ),
    "digitaltwins_isa95_OperationsSchedule_v1": (
        BFO + "0000031",
        "An operations schedule is a plan-like information specification.",
    ),
    "digitaltwins_isa95_OperationsRequest_v1": (
        BFO + "0000031",
        "An operations request is an information item specifying requested work.",
    ),
}


def text(element: ET.Element, path: str) -> str:
    return element.findtext(path, default="", namespaces=NS).strip()


def select_dockings(
    classes: list[ET.Element],
    bfo_classes: set[str],
) -> dict[str, tuple[str, str]]:
    source_terms = {
        element.get(f"{{{RDF}}}about", "").removeprefix(ISA95)
        for element in classes
    }
    missing = set(DOCKINGS) - source_terms
    if missing:
        raise ValueError(
            "Configured ISA-95 classes were not found in the input: "
            + ", ".join(sorted(missing))
        )

    invalid_targets = {
        bfo_iri
        for bfo_iri, _ in DOCKINGS.values()
        if bfo_iri not in bfo_classes
    }
    if invalid_targets:
        raise ValueError(
            "Configured BFO targets were not found in the local BFO source: "
            + ", ".join(sorted(invalid_targets))
        )

    return {name: docking for name, docking in DOCKINGS.items() if name in source_terms}


def build_alignment(
    classes: list[ET.Element],
    dockings: dict[str, tuple[str, str]],
) -> bytes:
    root = ET.Element(f"{{{RDF}}}RDF")
    ontology = ET.SubElement(
        root,
        f"{{{OWL}}}Ontology",
        {f"{{{RDF}}}about": ALIGNMENT},
    )
    ET.SubElement(ontology, f"{{{RDFS}}}label").text = "ISA-95 to BFO alignment"
    ET.SubElement(ontology, f"{{{RDFS}}}comment").text = (
        "Contains only ISA-95 terms with reviewed BFO dockings. The ISA-95 source ontology is not imported, "
        "so unmapped source terms are excluded from this ontology."
    )
    ET.SubElement(
        ontology,
        f"{{{OWL}}}imports",
        {f"{{{RDF}}}resource": BFO_ONTOLOGY},
    )
    ET.SubElement(ontology, f"{{{OWL}}}versionInfo").text = "Seed 0.1.0"

    for source_class in classes:
        source_iri = source_class.get(f"{{{RDF}}}about", "")
        local_name = source_iri.removeprefix(ISA95)
        docking = dockings.get(local_name)
        if docking is None:
            continue
        bfo_iri, rationale = docking
        mapped_class = ET.SubElement(
            root,
            f"{{{OWL}}}Class",
            {f"{{{RDF}}}about": source_iri},
        )
        ET.SubElement(
            mapped_class,
            f"{{{RDFS}}}subClassOf",
            {f"{{{RDF}}}resource": bfo_iri},
        )
        ET.SubElement(mapped_class, f"{{{RDFS}}}comment").text = rationale
        ET.SubElement(
            mapped_class,
            f"{{{RDFS}}}isDefinedBy",
            {f"{{{RDF}}}resource": ISA95},
        )

    raw = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    return minidom.parseString(raw).toprettyxml(indent="  ", encoding="utf-8")


def write_review_report(
    classes: list[ET.Element],
    dockings: dict[str, tuple[str, str]],
) -> tuple[int, int]:
    aligned = 0
    with REVIEW_FILE.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(
            output,
            fieldnames=("isa95_iri", "label", "definition", "isa95_parents", "bfo_docking", "status", "rationale"),
        )
        writer.writeheader()
        for element in classes:
            iri = element.get(f"{{{RDF}}}about", "")
            local_name = iri.removeprefix(ISA95)
            docking = dockings.get(local_name)
            parents = "; ".join(
                parent.get(f"{{{RDF}}}resource", "")
                for parent in element.findall("rdfs:subClassOf", NS)
            )
            if docking is None:
                bfo_iri, status, rationale = "", "needs-review", "No reviewed BFO docking is configured."
            else:
                bfo_iri, rationale = docking
                status = "reviewed"
                aligned += 1
            writer.writerow(
                {
                    "isa95_iri": iri,
                    "label": text(element, "rdfs:label"),
                    "definition": text(element, "rdfs:comment"),
                    "isa95_parents": parents,
                    "bfo_docking": bfo_iri,
                    "status": status,
                    "rationale": rationale,
                }
            )
    return aligned, len(classes) - aligned


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"{INPUT_FILE} not found; run tools/generate_isa95_rdf.py first."
        )

    source = ET.parse(INPUT_FILE).getroot()
    classes = source.findall("owl:Class", NS)
    if not classes:
        raise ValueError(f"No owl:Class terms found in {INPUT_FILE}")

    bfo_source = ET.parse(BFO_SOURCE_FILE).getroot()
    bfo_classes = {
        element.get(f"{{{RDF}}}about", "")
        for element in bfo_source.findall("owl:Class", NS)
    }
    dockings = select_dockings(classes, bfo_classes)

    OUTPUT_FILE.write_bytes(build_alignment(classes, dockings))
    aligned, needs_review = write_review_report(classes, dockings)
    print(f"Wrote {OUTPUT_FILE} with {aligned} reviewed BFO dockings")
    print(f"Wrote {REVIEW_FILE}; {needs_review} terms still need review")


if __name__ == "__main__":
    main()
