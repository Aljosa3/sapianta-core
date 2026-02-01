import json
from modules.llm_adapter.contract import LLMAdapter, LLMRequest


def extract_entities(
    input_payload: dict | str,
    llm: LLMAdapter,
) -> dict:
    if isinstance(input_payload, dict):
        input_text = str(input_payload)
    else:
        input_text = input_payload

    prompt = (
        "Extract only explicitly mentioned entities from the following input.\n"
        "Do not infer or interpret.\n"
        "Do not add entities that are not explicitly stated.\n\n"
        "Return a JSON object with the following keys only if present:\n"
        "- dates\n"
        "- amounts\n"
        "- actors\n"
        "- locations\n"
        "- documents\n\n"
        "Each value must be a list of strings.\n\n"
        f"Input:\n{input_text}"
    )

    request = LLMRequest(prompt=prompt)
    response = llm.generate(request)

    raw_output = response.text.strip()

    default_entities = {
        "dates": [],
        "amounts": [],
        "actors": [],
        "locations": [],
        "documents": [],
    }

    if not raw_output:
        return {"entities": default_entities}

    try:
        parsed = json.loads(raw_output)
        if not isinstance(parsed, dict):
            return {"entities": default_entities}

        entities = {}
        for key in default_entities:
            values = parsed.get(key, [])
            if isinstance(values, list):
                entities[key] = [
                    str(v).strip()
                    for v in values
                    if isinstance(v, (str, int, float)) and str(v).strip()
                ]
            else:
                entities[key] = []

        return {"entities": entities}

    except json.JSONDecodeError:
        return {"entities": default_entities}
