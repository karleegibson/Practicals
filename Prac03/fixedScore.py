def main():
    score = float(input("Enter score: "))
    valid_score_message = check_valid_score(score)
    print(valid_score_message)

def check_valid_score(score):
    if score < 0 or score > 100:
        message = "Invalid score"
    elif 50 < score <= 90:
        message = "Passable"
    elif score > 90:
        message = "Excellent"
    else:
        message = "Bad"
    return message


main()
