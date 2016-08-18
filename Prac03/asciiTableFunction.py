def main():
    lower = 10
    upper = 100
    numb = get_number(lower, upper)
    print(numb)
    #for i in range(10, 101):
    #print("{:<5d} {:<4}".format(i, chr(i)))

def get_number(lower, upper):
    finished = False
    while not finished:
        try:
            number = int(input("Enter a number (10-100): "))
            if (number < lower) or (number > upper):
                print("Sorry but number must be between 10 and 100")
                finished = False
            else:
                finished = True
                return number
        except ValueError:
            print("Must be a valid number")
            finished = False

main()