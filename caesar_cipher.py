def encrypt_letter(letter, shift):
    ascii_key = ord(letter)# Convert letter to ascii using ord
    shifted_ascii = ascii_key + shift # Shift new letter by adding shift value to the ascii key
    new_letter = chr(shifted_ascii) # Convert the new letter ascii key back to character form
    return new_letter # Return the converted letter

def main():
    '''
    Main entry of this program
    '''
    input_letter = input("Enter your letter: ")
    print(encrypt_letter(input_letter, 3))

if __name__ == "__main__":
    main()