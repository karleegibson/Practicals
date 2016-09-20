from Prac07.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name_of_guitar = input("Name: ")
    while name_of_guitar != "":
        name_of_guitar = Guitar(name_of_guitar)
        guitar_year = Guitar(year=int(input("Year: ")))
        guitar_cost = Guitar(cost=float(input("Cost: ")))
        guitars.append((name_of_guitar.name, guitar_year.year, guitar_cost.cost))
        print("{} ({}) : ${} added.".format(name_of_guitar.name, guitar_year.year, guitar_cost.cost))
        name_of_guitar = input("Name: ")
    print("These are my guitars:")
    count = 0
    for guitar in guitars:
        count += 1
        print("Guitar {}: {} ({}), worth ${}".format(count, guitar.name, guitar.year, guitar.cost))

main()
