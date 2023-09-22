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

def test_encrypt_message_hello():
    # Setup
    message = "HELLO"
    shift = 3
    expected = "KHOOR"

    # Invoke
    result = caesar_cipher.encrypt_message(message, shift)

    # Analyze
    assert result == expected

def test_encrypt_message_hello_low():
    # Setup
    message = "hello"
    shift = 3
    expected = ''

    # Invoke
    result = caesar_cipher.encrypt_message(message, shift)

    # Analyze
    assert result == expected

def test_encryot_message_long():
    # Setup
    message = "HELLOHELLO"
    shift = 3
    expected = "KHOORKHOOR"

    # Invoke
    result = caesar_cipher.encrypt_message(message, shift)

    # Analyze
    assert result == expected

def test_decrypt_message_khoor():
    # Setup
    message = "KHOOR"
    shift = 3
    expected = "HELLO"

    # Invoke
    result = caesar_cipher.decrypt_message(message, shift)

    # Analyze
    assert result == expected

def test_decrypt_message_khoorkhoor():
    # Setup
    message = "KHOORKHOOR"
    shift = 3
    expected = "HELLOHELLO"

    # Invoke
    result = caesar_cipher.decrypt_message(message, shift)

    # Analyze
    assert result == expected

def test_decrypt_message_khoor_default():
    # Setup
    message = "KHOOR"
    expected = "HELLO"

    # Invoke
    result = caesar_cipher.decrypt_message(message)

    # Analyze
    assert result == expected