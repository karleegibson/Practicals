in_file = open("numbers.txt", mode='r')

number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)

in_file.close()
