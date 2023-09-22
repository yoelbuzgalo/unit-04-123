import total_cost

def test_calculate_total_cost_5():
    # Setup
    x = 5
    expected = 250

    # Invoke
    result = total_cost.calculate_total_cost(x)

    # Analysis
    assert result == expected

def test_calculate_total_cost_17():
    # Setup
    x = 17
    expected = 765

    # Invoke
    result = total_cost.calculate_total_cost(x)

    # Analysis
    assert result == expected

def test_calculate_total_cost_23():
    # Setup
    x = 23
    expected = 874

    # Invoke
    result = total_cost.calculate_total_cost(x)

    # Analysis
    assert result == expected

def test_calculate_total_cost_35():
    # Setup
    x = 35
    expected = 1120

    # Invoke
    result = total_cost.calculate_total_cost(x)

    # Analysis
    assert result == expected