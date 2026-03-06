def run_constitutional_flow(domain):
    proposal = domain.create_proposal()

    advisory = domain.evaluate_policy(proposal)

    authority = domain.apply_authority(advisory)

    decision = domain.finalize_decision(authority)

    assert decision.hash is not None
    assert decision.replayable is True


def test_constitutional_flow_placeholder():
    """
    Placeholder test so pytest collects the file.
    Real domain adapters will call run_constitutional_flow().
    """
    assert True