class ProgrammingLanguage:
    def __init__(self, language='', typing='', year=0):
        self.language = language
        self.typing = typing
        self.reflection = True
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return self.reflection
        else:
            self.reflection = False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.language, self.typing, self.reflection,
                                                                           self.year)
