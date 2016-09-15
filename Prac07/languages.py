from Prac07.programminglanguage import ProgrammingLanguage


def main():
    dynamic_languages = []
    ruby = ProgrammingLanguage("Ruby", "Dynamic", 1995)
    python = ProgrammingLanguage("Python", "Dynamic", 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", 1991)
    # print(ruby)
    # print(python)
    # print(vb)

    print("The dynamically typed languages are:")
    languages = [ruby, python, vb]
    for language in languages:
        if language.is_dynamic():
            print(language.language)


main()
