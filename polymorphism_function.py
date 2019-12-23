class Parrot :

    def fly(self) :
        print("parrot can fly")
    def run(self) :
        print("parrot can't run")
    
class Dog :

    def fly(self) :
        print("dog can't fly")
    def run(self) :
        print("dog can run")

#common interface which is function
#class Parrot :

    def fly(self) :
        print("parrot can fly")
    def run(self) :
        print("parrot can't run")
    
class Dog :

    def fly(self) :
        print("dog can't fly")
    def run(self) :
        print("dog can run")

#common interface , function
# this is polymorphism
def Animal_fun(animal) :
    animal.fly()
   
#object of class
obb1 = Parrot()
obb2 = Dog()

# passing object to interface function 
Animal_fun(obb1)
Animal_fun(obb2)