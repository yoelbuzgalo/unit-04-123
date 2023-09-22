import group_characters

def test_is_upper_B():
    # Setup
    x = "B"
    expected = True

    # Invoke
    result = group_characters.is_upper(x)

    # Analysis
    assert result == expected

def test_is_upper_b():
    # Setup
    x = "b"
    expected =  False

    # Invoke
    result = group_characters.is_upper(x)

    # Analysis
    assert result == expected

def test_is_lower_c():
    # Setup
    x = "c"
    expected = True

    # Invoke
    result = group_characters.is_lower(x)

    # Analysis
    assert result == expected

def test_is_lower_C():
    # Setup
    x = "C"
    expected =  False

    # Invoke
    result = group_characters.is_lower(x)

    # Analysis
    assert result == expected

def test_is_digit_5():
    # Setup
    x = "5"
    expected = True

    # Invoke
    result = group_characters.is_digit(x)

    # Analysis
    assert result == expected

def test_is_digit_M():
    # Setup
    x = "M"
    expected =  False

    # Invoke
    result = group_characters.is_digit(x)

    # Analysis
    assert result == expected