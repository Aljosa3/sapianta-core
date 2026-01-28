# FILE: modules/ipv_v1_1/cli.py
# IPV-1.1 semantic mapper — audit CLI

import json
import sys
from modules.ipv_v1_1.semantic_mapper import SemanticMapperV1_1


def main():
    if len(sys.argv) != 2:
        print("Usage: ipv_semantic_cli '<json_input>'")
        sys.exit(1)

    raw = sys.argv[1]
    try:
        event = json.loads(raw)
    except json.JSONDecodeError:
        print("Invalid JSON input")
        sys.exit(2)

    mapper = SemanticMapperV1_1()
    result = mapper.map(event)

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
