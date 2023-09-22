def indexing():
    my_string = "honeymoons"
    length = len(my_string)
    print(len(my_string)) # Prints the length of my string
    print(my_string[0]) # First character
    print(my_string[length-1]) # Last character
    print(my_string[3]) # A letter in between
    print(my_string[4]) # Second letter in between
    print(my_string[-1]) # Last letter
    print(my_string[-10]) # First letter

def concat():
    empty_string = ''
    empty_string = empty_string + "H"
    empty_string = empty_string + "e"
    empty_string = empty_string + "l"
    empty_string = empty_string + "l"
    empty_string = empty_string + "o"
    print(empty_string)
    print(empty_string[0])

def main():
    indexing()
    concat()

if __name__ == "__main__":
    main()