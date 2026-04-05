class Students:
    def __init__(self):
        self.__id = 123  # Private variable
        self.__name = "Achman"  # Private variable

    def display(self):
        print(self.__name)
        print(self.__id)


s = Students()
s.display()
print(s._Students__id)      #Name Mangling
print(s._Students__name)      #Name Mangling
