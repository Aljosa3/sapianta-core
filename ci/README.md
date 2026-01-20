# CI Guard — Module Builder Enforcement

This CI guard enforces the rule:

No module may exist in the repository unless it was created
via the SAPIANTA Module Builder.

Detection mechanism:
- Each valid module directory MUST contain:
  `.module_builder_manifest`

Any module without this marker causes CI to fail.

This guard is:
- structural
- non-semantic
- SRS compliant
