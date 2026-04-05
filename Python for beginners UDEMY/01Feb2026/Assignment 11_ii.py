class Patient:
    def __init(self, id, name, ssn):
        self.__id = id
        self.__name = name
        self.__ssn = ssn

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSsn(self, ssn):
        self.__ssn = ssn

    def getSsn(self):
        return self.__ssn


p = Patient()
p.setId(123)
p.setName('John')
p.setSsn("123-456-7890")

print(p.getId())
print(p.getName())
print(p.getSsn())

print(p._Patient__id)
print(p._Patient__name)
print(p._Patient__ssn)