HEXADECIMAL_COLOUR_CODES_DICTIONARY = {"aquamarine1": "#7fffd4", "bisque1": "#ffe4c4", "brown3": "cd3333", "CadetBlue4": "53868b", "cyan1": "#00ffff"}

colour = input("Colour: ")
if colour not in HEXADECIMAL_COLOUR_CODES_DICTIONARY:
    print("Error!")
    colour = input("Colour: ")
print(HEXADECIMAL_COLOUR_CODES_DICTIONARY[colour])