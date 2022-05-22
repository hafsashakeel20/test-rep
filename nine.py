#9
class A:
    def __init__(self):
        self.x= 100
    def display(self):
        print("")
        print("X(from base) = ", self.x)
    #def display(self, z):
    #    print("X(from base) = ", self.x)
    #    print("Z value overloaded = ", z)

class B(A):
    def __init__(self):
        self.y=50
        A.__init__(self)
    def display(self):
        print("X(from derived) = ", self.x)
        print("Y(from derived) = ",self.y)
        print("Overiding achieved!")
    def dets(self):
        print("X and Y values are printed!")

objt3=A()
objt2=B()
print(objt2.x)
print(objt2.y)
#print(objt3.display(20))
print(objt3.display())
print(objt2.display())
print(objt2.dets())
