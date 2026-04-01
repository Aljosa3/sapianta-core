def test_add_logic_fixed():

    from runtime.development.generated.test_syntax import add

    result = add(2, 3)

    assert result == 10