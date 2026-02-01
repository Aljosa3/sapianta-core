from modules.llm_adapter.contract import LLMAdapter, LLMRequest


def extract_constraints(
    input_payload: dict | str,
    llm: LLMAdapter,
) -> dict:
    if isinstance(input_payload, dict):
        input_text = str(input_payload)
    else:
        input_text = input_payload

    prompt = f"""Extract only explicit constraints, limitations, obligations, prohibitions,
deadlines, or conditions that are directly stated in the input.
Do not interpret, infer, evaluate, or recommend.
Return each constraint as a short standalone sentence.

Input:
{input_text}"""

    request = LLMRequest(prompt=prompt)
    response = llm.generate(request)

    raw_output = response.text.strip()

    if not raw_output:
        return {"constraints": []}

    constraints = []
    lines = raw_output.split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith('- '):
            line = line[2:].strip()
        elif line.startswith('* '):
            line = line[2:].strip()
        elif line and line[0].isdigit() and '.' in line[:4]:
            parts = line.split('.', 1)
            if len(parts) > 1:
                line = parts[1].strip()

        if line:
            constraints.append(line)

    return {"constraints": constraints}
