def is_upper(character):
    '''
    This function returns True if character is upper case between A to Z
    '''
    return (character >= "A" and character <= "Z")

def is_lower(character):
    '''
    This function returns True if character is lower case between A to Z
    '''
    return (character >= "a" and character <= "z")

def is_digit(character):
    '''
    This function returns True if character string is a digit character, between 0 and 9
    '''
    return (character >= "0" and character <= "9")

def group_characters(characters):
    '''
    This function reorganizes characters in a characters string in a specific order; digits first, then lower case, then upper cases and returns it as a string
    '''
    digit_characters = '' # Initializes digit_characters variable to contain only digit characters
    lower_characters = '' # Initializes lower_characters variable to contain only lower case characters
    upper_characters = '' # Initializes upper_characters variable to contain only upper case characters
    for index in range(len(characters)):
        if is_digit(characters[index]):
            # Enters this block only if the character of the given index is a digit
            digit_characters += characters[index] # Adds the character to digit_characters variable group
            continue # Continues to the next iteration instead of continuing to next if blocks
        if is_lower(characters[index]):
            # Enters this block only if the character of the given index is a lower case
            lower_characters += characters[index] # Adds the character to lower_case variable group
            continue # Continues to the next iteration instead of continuing to next if blocks
        if is_upper(characters[index]):
            # Enters this block only if the character of the given index is an upper case
            upper_characters += characters[index] # Adds the character to upper_case variable group
    grouped_characters = digit_characters + lower_characters + upper_characters
    return grouped_characters

def main():
    '''
    Main entry of this program
    '''
    while True:
        user_string = input("Enter a string consisting of letters and digits: ")
        if user_string == '':
            break # Stops this loop immediately if the user enters an empty string
        print(group_characters(user_string)) # Otherwise, it will run this function normally - calling the group_characters function first then printing the returned values

if __name__ == "__main__":
    main()