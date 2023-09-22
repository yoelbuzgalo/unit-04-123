def count_down(number):
    sum = 0
    while number >= 0:
        print(number)
        sum += 1
        number += -1
    return sum

def count_up(number):
    sum = 0
    counter = 0
    while counter <= number:
        print(counter)
        sum += 1
        counter += 1
    return sum

def sum_of_odds():
    sum = 0
    while True:
        num = int(input("Enter a number: "))
        if num == 0:
            # exits out of this loop if the input is 0
            break
        if num % 2 == 0:
            # ignores and continues if its an even number
            continue
        else:
            sum += num
    return sum

def print_range(a_range):
    index = 0
    while index < len(a_range):
        print(a_range[index], end=' ')
        index += 1
    print()

def main():
    print("Number of prints:", count_down(5))
    print("Number of prints:", count_up(5))
    print(sum_of_odds())
    print_range(range(11))
    print_range(range(0,21, 2))
    print_range(range(5,16, 2))
    print_range(range(10,-1, -1))

if __name__ == "__main__":
    main()