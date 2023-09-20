import random

MINIMUM = -100
MAXIMUM = 100

def absolute_difference(a, b):
    '''
    This function returns an absolute difference between two passed integers
    '''
    if a > b:
        # If a is greater than b, it will enter this block
        return a - b # Returns the difference between a and b
    return b - a # Otherwise it will return the difference between b and a (b is greater than a)

def main():
    '''
    Main entry of this program
    '''
    # Generate two random integers using the global constants of -100 and 100
    random_num_1 = random.randint(MINIMUM, MAXIMUM)
    random_num_2 = random.randint(MINIMUM, MAXIMUM)
    
    # Calling absolute difference function and printing out the result
    print("a=", random_num_1,","," b=",random_num_2," absolute difference=", absolute_difference(random_num_1, random_num_2),sep="")

if __name__ == "__main__":
    # Guard clause to prevent accidental run if I were to run pytest for practice_test.py
    main()