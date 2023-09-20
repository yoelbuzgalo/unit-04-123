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

def test_is_alphabetic_exclamation():
    # Setup
    letter = "!"
    expected = False

    # Invoke
    result = caesar_cipher.is_alphabetic(letter)

    # Analyze
    assert result == expected

def test_is_alphabetic_A():
    # Setup
    letter = "A"
    expected = True

    # Invoke
    result = caesar_cipher.is_alphabetic(letter)

    # Analyze
    assert result == expected

def test_encrypt_letter_nonalphabetic():
    # Setup
    letter = "*"
    shift = 3
    expected = ''

    # Invoke
    result = caesar_cipher.encrypt_letter(letter,shift)

    # Analyze
    assert result == expected

def test_decrypt_letter_A_3():
    # Setup
    letter = "D"
    shift = 3
    expected = "A"

    # Invoke
    result = caesar_cipher.decrypt_letter(letter, shift)

    # Analyze
    assert result == expected

def test_decrypt_letter_G_5():
    # Setup
    letter = "L"
    shift = 5
    expected = "G"

    # Invoke
    result = caesar_cipher.decrypt_letter(letter, shift)

    # Analyze
    assert result == expected

def test_decrypt_letter_D_10():
    # Setup
    letter = "N"
    shift = 10
    expected = "D"

    # Invoke
    result = caesar_cipher.decrypt_letter(letter, shift)

    # Analyze
    assert result == expected

def test_decrypt_letter_nonalphabetic():
    # Setup
    letter = "*"
    shift = 3
    expected = ''

    # Invoke
    result = caesar_cipher.decrypt_letter(letter,shift)

    # Analyze
    assert result == expected
