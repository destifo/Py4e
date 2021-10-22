class DataScientist:
    name = ""
    age = 0

    def __init__(self):
        print("constructed")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        print("namaye wa:", self.name)
    def getage(self):
        print("shiranye kedo: ", self.age)
    def setname(self, name):
        print("current name: ", self.name)
        self.name = name
        print("new name:", self.name)
    def setage(self, age):
        self.age = age


dest = DataScientist()
#dest.setname("estifanos")
#dest.getage()
