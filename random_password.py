def create_ascii_range_string(start, stop):
    '''
    This function creates and returns a string consisting of consectutive characters from the start value (inclusive) up to the stop value (exclusive)
    '''
    ascii_string = ""
    for ascii_value in range(start, stop):
        ascii_key = chr(ascii_value)
        ascii_string += ascii_key
    return ascii_string

