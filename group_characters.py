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