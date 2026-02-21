from runtime.chat_shell_hds.hoi_guard import HOIGuard
from runtime.chat_shell_hds.llm_stub import DummyLLM as BaseLLM
from runtime.chat_shell_hds.hds_engine import HDSEngine as BaseHDS

from .hds_engine import HDSEngine
from .llm_stub import DummyLLM
from .models import OptionProposal


def main():
    hoi = HOIGuard()

    # osnovni v0.1 generator možnosti (ne spreminjamo)
    base_hds = BaseHDS(BaseLLM())
    explain_hds = HDSEngine(DummyLLM())

    last_options: list[OptionProposal] = []

    print("SAPIANTA — HDS Chat Shell v0.2 (Explain-on-Demand)")
    print("Ukazi: why <n> | expand <n> | uncertainty <n> | exit\n")

    while True:
        try:
            raw = input(">> ").strip()

            if raw.lower() == "exit":
                break

            if not hoi.ensure_legitimacy():
                print("HOI: REDIRECT — dialog ni obdelan.")
                continue

            # explain-on-demand
            if raw.startswith(("why ", "expand ", "uncertainty ")):
                if not last_options:
                    print("Ni predhodnih možnosti za razlago.")
                    continue

                mode, idx = raw.split(maxsplit=1)
                i = int(idx) - 1

                if i < 0 or i >= len(last_options):
                    print("Neveljavna izbira.")
                    continue

                explanation = explain_hds.explain(last_options[i], mode)
                print(f"\nRazlaga ({mode}): {explanation}\n")
                print("Opomba: Odločitev je vedno na človeku.\n")
                continue

            # nova vprašanja → nove možnosti
            last_options = base_hds.analyze(raw)

            print("\n— Predlagane možnosti (HDS) —\n")
            for idx, p in enumerate(last_options, start=1):
                print(f"[{idx}] {p.title}")
                print(f"  Razlog: {p.rationale}")
                print("  Posledice:")
                for c in p.consequences:
                    print(f"   - {c}")
                print(f"  Negotovost: {p.uncertainty}\n")

            print("Opomba: Odločitev je vedno na človeku.\n")

        except RuntimeError as e:
            print(str(e))
            break


if __name__ == "__main__":
    main()
