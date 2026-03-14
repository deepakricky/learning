#super() method is used to access the methods of a super class in the derived class.

class A: #parent class
    a=1
    def __init__(self):
        print("The class is A")

class B(A): #child1 class
    b=2
    def __init__(self):
        print("The class is B")

class C(B):  #child2 class
    c=3
    def __init__(self):
        super().__init__()
        print("The class is C")

o=C()
print(o.a, o.b, o.c) # here C contains att of A , B and C
