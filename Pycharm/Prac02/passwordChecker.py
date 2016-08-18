"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    count_lower = sum([int(char.islower()) for char in password])
    if count_lower == 0:
        return False
    count_upper = sum([int(char.isupper()) for char in password])
    if count_upper == 0:
        return False
    length = len(password)
    if length < 2 or length > 6:
        return False
    count_digit = sum([int(char.isdigit()) for char in password])
    if count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED:
        count_special = sum([int(char.isspecial()) for char in password])
        if count_special == 0:
            return False
    return True


main()
