class Bird :
    def intro(self) :
        print("This is introduction of birds")
#inheritance use Sparrow
class Sparrow(Bird) :

    def fly(self) :
        print("Sparrow can fly")

class Ostrich(Bird) :

    def fly(self) :
        print("ostrich can't FLY")
    
obb1 = Bird()
obb2 = Sparrow()
obb3 = Ostrich()

obb1.intro()

obb2.intro()
obb2.fly()

obb3.intro()
obb3.fly()