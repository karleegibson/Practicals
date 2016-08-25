def main():
    numbers = []
    numb_numbers = int(input("How many numbers? "))

    for number in range(1, numb_numbers + 1):
        new_number = int(input("Enter number {}: ".format(number)))
        numbers.append(new_number)

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format((sum(numbers)) / numb_numbers))


main()