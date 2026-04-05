class Patient:
    def __init__(self):
        self.__id = 101
        self.__name = "Anubhav"
        self.__ssn = 123123123
    def setId(self,id):
        self.__id = id
    def getId(self):
        return self.__id
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setSsn(self,ssn):
        self.__ssn = ssn
    def getSsn(self):
        return self.__ssn

P1 = Patient()
print(P1._Patient__id)      #Name Mangling
print(P1._Patient__name)
print(P1._Patient__ssn)

P2 = Patient()
P2.setId(102)
P2.setName("Achman")
P2.setSsn(111222333)
print(P2.getId())
print(P2.getName())
print(P2.getSsn())