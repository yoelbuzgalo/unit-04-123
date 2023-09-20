import caesar_cipher

def test_encrypt_letter_A_3():
    # Setup
    letter = "A"
    shift = 3
    expected = "D"

    # Invoke
    result = caesar_cipher.encrypt_letter(letter, shift)

    # Analyze
    assert result == expected

def test_encrypt_letter_G_5():
    # Setup
    letter = "G"
    shift = 5
    expected = "L"

    # Invoke
    result = caesar_cipher.encrypt_letter(letter, shift)

    # Analyze
    assert result == expected

def test_encrypt_letter_D_10():
    # Setup
    letter = "D"
    shift = 10
    expected = "N"

    # Invoke
    result = caesar_cipher.encrypt_letter(letter, shift)

    # Analyze
    assert result == expected

