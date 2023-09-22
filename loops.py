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

def main():
    print("Number of prints:", count_down(5))
    print("Number of prints:", count_up(5))

if __name__ == "__main__":
    main()