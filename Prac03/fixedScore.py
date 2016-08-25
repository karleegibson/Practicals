def main():
    score = float(input("Enter score: "))
    valid_score_message = calc_result(score)
    print(valid_score_message)

def calc_result(score):
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
