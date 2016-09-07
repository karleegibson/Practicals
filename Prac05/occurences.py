
text = input("Text: ").split()
text_dictionary = {}
for word in text:
    if word in text_dictionary:
        text_dictionary[word] += 1
    else:
        text_dictionary[word] = 1
sorted(text_dictionary)
for key, value in text_dictionary.items():
    print("{:{}} : {}".format(key, 15, value))