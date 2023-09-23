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

def generate_random_password(uppercase_num, lowercase_num, digits_num, symbols_num):
    '''
    This function generates a random password string given passed parameters of how many characters of each type they want; uppercase, lowercase, digits or symbols
    '''
    # Stores each required number of characters in password string in a counter variable for the generator to keep track of
    uppercase_counter = uppercase_num
    lowercase_counter = lowercase_num
    digits_counter = digits_num
    symbols_counter = symbols_num
    
    # Initializes variable containers for generators to update and concatenate accordingly
    password_string = ""

    # A while loop to keep track of generating each type of character required by the user input
    while uppercase_counter > 0 or lowercase_counter > 0 or digits_counter > 0 or symbols_counter > 0:
        randomizer = random.randrange(0, 4) # Generates a random number between 0 to 3 (4 not inclusive)
        if randomizer == 0 and uppercase_counter > 0:
            # If 0, it'll choose a random character from uppercase
            password_string += get_random_char_from_string(create_uppercase_letters_string())
            uppercase_counter += -1
        elif randomizer == 1 and lowercase_counter > 0:
            # If 1, it'll choose a random character from lowercase
            password_string += get_random_char_from_string(create_lowercase_letters_string())
            lowercase_counter += -1
        elif randomizer == 2 and digits_counter > 0:
            # If 2, it'll choose a random character from digits
            password_string += get_random_char_from_string(create_digits_string())
            digits_counter += -1
        elif randomizer == 3 and symbols_counter > 0:
            # If 3, it'll choose a random character from symbols
            password_string += get_random_char_from_string(create_symbols_string())
            symbols_counter += -1
    
    return password_string # Once complete, itll return the password string


def main():
    while True:
        user_input = input("Enter <num uppers> <num lowers> <num digits> <num symbols>: ")
        values = user_input.split()
        if user_input == '':
            # If user enters an empty string, then the program will exit immediately
            break
        elif len(values) != 4:
            print("You must enter exactly 4 values")
        else:
            uppercase_val = 0
            lowercase_val = 0
            digits_val = 0
            symbols_val = 0
            for index in range(len(values)):
                if index == 0:
                    uppercase_val += int(values[index])
                elif index == 1:
                    lowercase_val += int(values[index])
                elif index == 2:
                    digits_val += int(values[index])
                elif index == 3:
                    symbols_val += int(values[index])
            print("Password:",generate_random_password(uppercase_val, lowercase_val, digits_val, symbols_val))

if __name__ == "__main__":
    main()
