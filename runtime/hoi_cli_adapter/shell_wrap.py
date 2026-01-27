from runtime.chat_shell_hds.hoi_guard import HOIGuard
from runtime.chat_shell_hds.hds_engine import HDSEngine
from runtime.chat_shell_hds.llm_stub import DummyLLM
from runtime.hoi_cli_adapter.adapter import HOICLIAdapter


def main():
    hoi = HOIGuard()
    hds = HDSEngine(DummyLLM())
    cli = HOICLIAdapter(hoi)

    print("SAPIANTA — HDS Chat Shell + HOI CLI Adapter")
    print("HOI ukazi: :pause | :orient | :redirect | exit\n")

    while True:
        try:
            raw = input(">> ")

            if raw.lower() == "exit":
                break

            # HOI ima absolutno prednost
            if cli.handle(raw):
                continue

            # legitimnostni prehod
            if not hoi.ensure_legitimacy():
                print("HOI: REDIRECT — dialog ni obdelan.")
                continue

            proposals = hds.analyze(raw)

            print("\n— Predlagane možnosti (HDS) —\n")
            for idx, p in enumerate(proposals, start=1):
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
