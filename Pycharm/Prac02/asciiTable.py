def main():
    lower = 10
    upper = 100
#print('Enter a number ({} - {}):'.format(lower, upper))
    for i in range(10, 101):
    print("{:<5d} {:<4}".format(i, chr(i)))

def get_number(lower, upper):
    try:
        number = int(input("Enter a number (10-100): "))
        while (number < lower) or (number > upper):
            print("Sorry but number must be between 10 and 100")
            number = int(input("Enter a number (10-100): "))
    except ValueError:
        print("Must be a valid number")


main()