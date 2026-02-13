"""
Deterministic Prompt Template Definitions.

No dynamic template construction.
No runtime interpolation.
No conditional branching.
"""

TEMPLATE_VERSION = "v1.0-deterministic"

PROMPT_TEMPLATE_STRUCTURE = {
    "header": "SAPIANTA_CANONICAL_EXPORT",
    "body_fields": [
        "state_name",
        "state_snapshot",
    ],
    "footer": "END_OF_EXPORT",
}
