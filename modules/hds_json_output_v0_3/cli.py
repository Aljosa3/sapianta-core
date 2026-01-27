import json
from schema import hds_json_schema
from explain import explain_on_demand


def main():
    # Deterministic placeholder options (no ranking, no signals)
    options = [
        {
            "id": "opt-1",
            "title": "Proceed conservatively",
            "rationale": "Maintains system stability under uncertainty.",
            "consequences": [
                "Lower short-term gain",
                "Reduced risk exposure"
            ],
            "uncertainty": "Medium"
        },
        {
            "id": "opt-2",
            "title": "Delay decision",
            "rationale": "Allows additional human assessment.",
            "consequences": [
                "Opportunity cost",
                "Improved contextual clarity"
            ],
            "uncertainty": "Low"
        }
    ]

    output = hds_json_schema(options)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
