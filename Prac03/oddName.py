"""Karlee Gibson"""

def main():
    get_name()


def get_name():
    name = input("Name: ")
    while name == "":
        print("Sorry but you can't leave name blank")
        name = input("Name: ")
    length = len(name)
    print(name[0:length:2])


main()