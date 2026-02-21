from .hoi_guard import HOIGuard
from .hds_engine import HDSEngine
from .llm_stub import DummyLLM


def main():
    hoi = HOIGuard()
    hds = HDSEngine(DummyLLM())

    print("SAPIANTA — HDS Chat Shell (READ-ONLY)")
    print("Odločitev je vedno na človeku.\n")

    while True:
        try:
            if not hoi.ensure_legitimacy():
                print("HOI: REDIRECT — dialog preusmerjen.")
                continue

            question = input("Vprašanje (ali 'exit'): ")
            if question.lower() == "exit":
                break

            proposals = hds.analyze(question)

            print("\n— Predlagane možnosti (HDS) —\n")
            for idx, p in enumerate(proposals, start=1):
                print(f"[{idx}] {p.title}")
                print(f"  Razlog: {p.rationale}")
                print("  Posledice:")
                for c in p.consequences:
                    print(f"   - {c}")
                print(f"  Negotovost: {p.uncertainty}\n")

            print("Opomba: Sistem ne sprejema odločitev namesto vas.\n")

        except RuntimeError as e:
            print(str(e))
            break


if __name__ == "__main__":
    main()
