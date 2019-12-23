class Person :
    def __init__(self,name) :
        self.name=name 
    def getName(self) :
        return self.name
    def isEmployee(self) :
        return False

class Employee(Person) :
    def isEmployee(self) :
        return True
obb1 = Person("parwej")
print(obb1.getName(),obb1.isEmployee())
obb2 = Employee("asfaque")
print(obb2.getName(),obb2.isEmployee())