from Prac07.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1992, 16035.40)
    print(gibson.get_age())
    print(gibson.is_vintage())

main()
