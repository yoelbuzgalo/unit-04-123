import random_password

def test_create_ascii_range_string_97_100():
    # Setup
    start = 97
    stop = 100
    expected = "abc"

    # Invoke
    result = random_password.create_ascii_range_string(start, stop)

    # Analysis
    assert result == expected

def test_create_uppercase_letters_string():
    # Setup
    expected = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Invoke
    result = random_password.create_uppercase_letters_string()

    # Analysis
    assert result == expected

def test_create_lowercase_letters_string():
    # Setup
    expected = "abcdefghijklmnopqrstuvwxyz"

    # Invoke
    result = random_password.create_lowercase_letters_string()

    # Analysis
    assert result == expected

def test_create_digits_string():
    # Setup
    expected = "0123456789"

    # Invoke
    result = random_password.create_digits_string()

    # Analysis
    assert result == expected

def test_create_symbols_string():
    # Setup
    expected = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    # Invoke
    result = random_password.create_symbols_string()

    # Analysis
    assert result == expected

def test_get_random_char_from_string_abc():
    # Setup
    string = "abc"
    expected_1 = "a"
    expected_2 = "b"
    expected_3 = "c"

    # Invoke
    result = random_password.get_random_char_from_string(string)

    # Analysis
    assert result == expected_1 or result == expected_2 or result == expected_3