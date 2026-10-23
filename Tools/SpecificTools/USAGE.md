# ISA-95 to BFO Alignment Usage

## Generate the artifacts

Run both commands from the repository root with Python 3.9 or newer. The scripts use only the Python standard library.

```text
python3 tools/generate_isa95_rdf.py
python3 tools/align_isa95_bfo.py
```

The second command requires `generated/isa95.rdf`, so regenerate that file first whenever the ISA-95 DTDL source changes.

## Outputs

- `generated/isa95.rdf` is the generated ISA-95 reference ontology. Do not add BFO axioms to this file or edit it manually.
- `generated/isa95-bfo-alignment.rdf` is a separate ontology importing canonical BFO only. It contains only ISA-95 terms with reviewed `rdfs:subClassOf` mappings, preserves their original IRIs, and marks the ISA-95 ontology as their source without importing its unmapped terms.
- `generated/isa95-bfo-review.csv` lists every generated ISA-95 class, its definition, ISA-95 parents, BFO docking (if reviewed), and review status.

## Review a docking

The `DOCKINGS` table in `tools/align_isa95_bfo.py` contains explicit mappings keyed by the generated ISA-95 class IRI suffix. Each entry provides a canonical BFO class IRI and a rationale. Review the source definition and intended meaning before adding an entry. The script fails if a configured ISA-95 class is absent from the generated ontology or its BFO target is absent from the local BFO source.

Terms without an entry are written to the CSV with status `needs-review`; they receive no BFO subclass axiom. Do not infer a BFO category from a technical ISA-95 superclass such as `BaseModel`, and do not add a generic `BFO:Entity` parent simply to make a term appear grounded. A term whose physical, informational, or process meaning is ambiguous should remain in the review queue until clarified.

After changing the docking table or source data, rerun both commands and inspect the generated alignment and review CSV. These generated files are reproducible outputs, not editing surfaces.
