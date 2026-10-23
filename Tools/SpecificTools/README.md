# Modeling Tooling

This area will contain reproducible commands for importing or normalizing ISA-95 material, validating source ontologies, running competency-question tests, generating diagrams, and packaging releases.

Keep environment setup and tool versions explicit. A future CI pipeline should run parse checks, SHACL validation, query regression tests, and generated-artifact checks on every model change.

## Generate ISA-95 RDF/XML

Run `python3 tools/generate_isa95_rdf.py` from the repository root. The converter reads all `*.json` files below `ontology/isa95/source/ISA95/` and writes `generated/isa95.rdf`, which can be opened and edited in Protégé as an RDF/XML ontology.

## Generate ISA-95 to BFO alignment

After generating `generated/isa95.rdf`, run `python3 tools/align_isa95_bfo.py`.
The script writes a separate `generated/isa95-bfo-alignment.rdf` containing
reviewed BFO subclass mappings; it does not modify the ISA-95 reference
ontology. It also writes `generated/isa95-bfo-review.csv` with every ISA-95
class and its mapping status. Add or revise mappings in the script only after
reviewing each term's definition and intended BFO category. Unmapped classes
remain marked `needs-review` rather than receiving a speculative parent.

See [USAGE.md](USAGE.md) for the complete workflow and review guidance.

## Generate IOF aggregate OWL

Run `python3 tools/generate_iof26_owl.py` from the repository root. The
converter gathers locally available released IOF ontology import closures
from `ontology/iof26/source/ontology-master/` and writes
`generated/iof26.owl`. The aggregate ontology IRI is
`https://schema.trumpf.com/testing/iof26/`; imported source term IRIs are
preserved. Generation fails if an import cannot be resolved from the local
source tree or its XML catalogs.
