import random

number_of_quick_picks = int(input("How many quick picks? "))
random.seed(1)
for i in range(number_of_quick_picks):
    random_numbers = []
    for element in range(6):
        random_number = random.randint(1, 45)
        random_numbers.append(random_number)
    random_numbers.sort()
    print(random_numbers)


