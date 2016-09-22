from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar


def main():
    prius1 = Taxi("Prius 1", 100)
    prius1.drive(40)
    print(prius1)

    prius1.start_fare()
    prius1.drive(100)
    print(prius1)
    print(prius1.get_fare())

    honda = UnreliableCar("Honda", 100, 55.59)
    honda.drive(40)
    print(honda)


main()
