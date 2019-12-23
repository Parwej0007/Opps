class Base :
    def __init__(self,name) :
        self.name=name
    def getName(self) :
        return self.name
        
class Child1(Base) :
    def __init__(self,name,age) :
        self.age=age
        Base.__init__(self,name)
    def getAge(self) :
        return self.age

class Child2(Base) :
    def __init__(self,name,phone) :
        self.phone=phone
        Base.__init__(self,name)
    def getPhone(self) :
        return self.phone
#Both child class access parent class data
obb1 = Child1(22,"parwej")
print(obb1.getAge(),obb1.getName())

obb2=Child2("Asfaque",8863883424)
print(obb2.getName(),obb2.getPhone())