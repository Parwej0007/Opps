class Base1 :
    def __init__(self) :
        self.str1="geek1"
        print("Base 1")

class Base2 :
    def __init__(self) :
        self.str2="geek2"
        print("Base 2")

class Child(Base1,Base2) :
    def __init__(self) :
        #calling constructor of base1 & base2 class
        Base1.__init__(self)
        Base2.__init__(self)
        print("child class")

    def StrPrint(self) :
        print(self.str1,self.str2)

obb1 = Child()
obb1.StrPrint()