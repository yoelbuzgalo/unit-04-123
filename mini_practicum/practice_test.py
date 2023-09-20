import practice

def test_absolute_difference_a_larger():
    # Setup
    x = 20
    y = 10
    expected = 10

    # Invoke
    result = practice.absolute_difference(x, y)

    # Analyze
    assert result == expected

def test_absolute_difference_b_larger():
    # Setup
    x = 10
    y = 20
    expected = 10

    # Invoke
    result = practice.absolute_difference(x, y)

    # Analyze
    assert result == expected

def test_absolute_difference_minus():
    # Setup
    x = -10
    y = -20
    expected = 10

    # Invoke
    result = practice.absolute_difference(x, y)

    # Analyze
    assert result == expected

def test_absolute_difference_zero():
    # Setup
    x = 10
    y = 10
    expected = 0

    # Invoke
    result = practice.absolute_difference(x, y)

    # Analyze
    assert result == expected