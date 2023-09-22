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