class Students:
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

s = Students()
s.setId(20)
s.setName("Anubhav")

print(s.getId())
print(s.getName())
