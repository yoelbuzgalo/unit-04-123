def calculate_total_cost(quantity):
    '''
    This function calculates the total cost depending on the quantity passed to this function.

    '''
    
    total_cost = 0 # Initializes a variable called total_cost to contain the total cost computation of this function
    
    if quantity >= 1 and quantity <= 9:
        # between 1 and 9, it will calculate the cost per item; 50
        total_cost = quantity * 50 # Updates the cost of total_cost
    elif quantity >= 10 and quantity <= 19:
        # between 10 and 19, it will calculate the cost per item; 45
        total_cost = quantity * 45
    elif quantity >= 20 and quantity <= 29:
        # between 20 and 29, it will calculate the cost per item; 38
        total_cost = quantity * 38
    elif quantity >= 30:
        # 30 and above, it will calculate the cost per item; 32
        total_cost = quantity * 32
    
    return total_cost

def main():
    '''
    Main entry of this program
    '''
    while True:
        # Prompts the user to enter a quantity
        user_input = int(input("Enter a quantity to be purchased: "))
        if user_input <= 0:
            break # Exits the program immediately if the user input is negative or equal to zero
        print("Total cost:", calculate_total_cost(user_input)) # Otherwise, it will normally call the function calculate_total_cost and print the returned value

if __name__ == "__main__":
    main()
    