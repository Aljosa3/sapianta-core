def test_ftl_repair_add():

    from runtime.development.dev_orchestrator import DevOrchestrator

    orch = DevOrchestrator()

    result = orch.repair("runtime/development/generated/test_add_failure.py")

    assert result["success"] is True