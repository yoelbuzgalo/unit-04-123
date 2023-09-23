import random

def create_ascii_range_string(start, stop):
    '''
    This function creates and returns a string consisting of consectutive characters from the start value (inclusive) up to the stop value (exclusive)
    '''
    ascii_string = ""
    for ascii_value in range(start, stop):
        ascii_key = chr(ascii_value)
        ascii_string += ascii_key
    return ascii_string

def create_uppercase_letters_string():
    '''
    This function creates and returns a string between A to Z (upper case)
    '''
    # Calls create_ascii_range_string to create a string between A to Z and stores them in the variable uppercase_letters_string
    uppercase_letters_string = create_ascii_range_string(65, 91)
    return uppercase_letters_string # Returns the created uppercase letters string

def create_lowercase_letters_string():
    '''
    This function creates and returns a string between a to z (lower case)
    '''
    # Calls create_ascii_range_string to create a string between a to z and stores them in the variable lowercase_letters_string
    lowercase_letters_string = create_ascii_range_string(97, 123)
    return lowercase_letters_string # Returns the created lowercase letters string

def create_digits_string():
    '''
    This function creates and returns a string between 0 to 9 (digit only)
    '''
    # Calls create_ascii_range_string to create a string between 0 to 9 and stores them in the variable digits_string
    digits_string = create_ascii_range_string(48, 58)
    return digits_string # Returns the created digits string


def create_symbols_string():
    '''
    This function creates and returns a string between ! to ~ (symbols only)
    '''

    # Calls for each range in ascii table that has symbols and stores them in variables
    symbols_string_1 = create_ascii_range_string(33,48)
    symbols_string_2 = create_ascii_range_string(58,65)
    symbols_string_3 = create_ascii_range_string(91, 97)
    symbols_string_4 = create_ascii_range_string(123,127)

    # Concatate all of the symbol strings together
    symbols_string = symbols_string_1+symbols_string_2+symbols_string_3+symbols_string_4
    return symbols_string # Returns the created symbols string

def get_random_char_from_string(string):
    '''
    This function gets a random character from a string is passed to this function
    '''
    # Generates a random number given a range between 0 to the max length of a string
    random_num = random.randrange(0, len(string))
    return string[random_num] # Returns the random picked number in the string