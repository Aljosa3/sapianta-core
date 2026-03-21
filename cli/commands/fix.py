import traceback

from runtime.development.repair_orchestrator import main as repair_main


def run(args=None):
    print("\n[SAPIANTA] FIX START\n")

    try:
        repair_main()

        print("\n[SAPIANTA] FIX COMPLETE\n")

    except Exception as e:
        print("\n[SAPIANTA] FIX ERROR")
        print("-----------------------------------")
        print(str(e))
        traceback.print_exc()