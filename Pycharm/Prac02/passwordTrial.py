password = input("> ")
#count_lower = 0
count_upper = 0
count_digit = 0
count_special = 0
#for char in password:
    #if char.islower():
        #count_lower += 1
#print(count_lower)

count_lower = sum([int(char.islower()) for char in password])
print(count_lower)
