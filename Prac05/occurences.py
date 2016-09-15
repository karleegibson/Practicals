
text = input("Text: ").split()
text_dictionary = {}
for word in text:
    if word in text_dictionary:
        text_dictionary[word] += 1
    else:
        text_dictionary[word] = 1
for word in sorted(text_dictionary):
    print("{:{}} : {}".format(word, 15, text_dictionary[word]))