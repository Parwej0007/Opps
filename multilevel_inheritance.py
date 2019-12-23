class Parent :
    def __init__(self,name) :
        self.name=name
    def getName(self) :
        print(self.name)

class Child(Parent) :
    def __init__(self,name,age) :
        #invoke parent name
        Parent.__init__(self,name)
        self.age=age
    def getAge(self) :
        print(self.age)

class GrandChild(Child) :
    def __init__(self,name,age,address) :
        self.address=address
        Child.__init__(self,name,age)
    def getAddress(self) :
        print(self.address)

obb1 = GrandChild("parwej",25,"BTM")
obb1.getName()
obb1.getAge()
obb1.getAddress()