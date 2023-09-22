def encrypt_letter(letter, shift):
    if is_alphabetic(letter):
        ascii_key = ord(letter)# Convert letter to ascii using ord
        shifted_ascii = ascii_key + shift # Shift new letter by adding shift value to the ascii key
        new_letter = chr(shifted_ascii) # Convert the new letter ascii key back to character form
        return new_letter # Return the converted letter
    else:
        return ''
    
def decrypt_letter(letter, shift):
    ascii_key = ord(letter)# Convert letter to ascii using ord
    shifted_ascii = ascii_key - shift # Shift new letter by subtracting shift value to the ascii key
    decrypted_letter = chr(shifted_ascii) # Convert the new letter ascii key back to character form
    if is_alphabetic(decrypted_letter):
        return decrypted_letter
    else:
        return ''

def is_alphabetic(character):
    return (character >= "A" and character <= "Z")

def encrypt_message(message, shift):
    ciphertext = ''
    
    ciphertext = ciphertext + encrypt_letter(message[0], shift)
    ciphertext = ciphertext + encrypt_letter(message[1], shift)
    ciphertext = ciphertext + encrypt_letter(message[2], shift)
    ciphertext = ciphertext + encrypt_letter(message[3], shift)
    ciphertext = ciphertext + encrypt_letter(message[4], shift)
    
    return ciphertext

def main():
    '''
    Main entry of this program
    '''
    input_letter = input("Enter your letter: ")
    print(encrypt_letter(input_letter, 3))

if __name__ == "__main__":
    main()