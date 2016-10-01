from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ")
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for taxi in taxis:
                print(taxi)
            taxi_choice = input("Choice taxi: ")

        choice = input(">>> ")
        if choice == "d":
            distance = int(input("Drive how far? "))
            taxi.drive(distance)

main()
