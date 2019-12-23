# operator overloading
# when we want to add two object using unary operator(+) then throw an error because interpreter does not knowo how to add unary operator
# So using __add__ operator known as operator overloading.

class opertor_overloading :

    def __init__(self,m1,m2) :
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other) :
        m1=self.m1 + other.m1
        m2=self.m2 +other.m2
        #m3= m1 + m2
        return m1,m2

obb1 = opertor_overloading(10,20)
obb2 = opertor_overloading(30,40)

m3=opertor_overloading.__add__(obb1,obb2)
#m3 = obb1 + obb2
print(m3)
