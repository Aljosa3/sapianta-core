# PATH: sapianta_chat/interface/cli_proposal_gate.py

from typing import Dict, Any, List


def proposal_gate(response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Human-in-the-loop proposal gate.

    The system MAY propose.
    The human MUST decide.

    This function:
    - performs NO execution
    - performs NO system-side effects
    - performs NO automatic approval
    """

    mode = response.get("mode")

    # Če odgovor ni proposal-only, ga prepustimo nespremenjenega
    if mode != "PROPOSAL_ONLY":
        return response

    content = response.get("content", {})
    proposals: List[Dict[str, Any]] = content.get("build_proposals", [])

    if not proposals:
        return response

    approved = []
    rejected = []
    modified = []

    print("\n────────────────────────────────────────")
    print("BUILD PROPOSAL REVIEW (human-in-the-loop)")
    print("────────────────────────────────────────\n")

    for idx, proposal in enumerate(proposals, start=1):
        description = proposal.get("description", "")

        print(f"Step {idx}:")
        print(description)
        print()

        while True:
            print("Choose action:")
            print("[a] approve")
            print("[m] modify")
            print("[r] reject")
            choice = input("> ").strip().lower()

            if choice == "a":
                approved.append(proposal)
                break

            if choice == "r":
                rejected.append(proposal)
                break

            if choice == "m":
                print("Enter modified description:")
                new_desc = input("> ").strip()

                modified.append({
                    **proposal,
                    "description": new_desc,
                })
                break

            print("Invalid input. Please choose [a], [m], or [r].")

        print()

    print("────────────────────────────────────────")
    print("REVIEW COMPLETE")
    print("────────────────────────────────────────\n")

    # Pasiven rezultat pregleda (brez izvrševanja)
    return {
        "mode": "PROPOSAL_REVIEW_RESULT",
        "content": {
            "approved": approved,
            "rejected": rejected,
            "modified": modified,
            "invariants": [
                "human_in_the_loop",
                "non_executable",
                "no_auto_decision",
            ],
        },
        "original_response": response,
    }
