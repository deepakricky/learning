# we take parent class > child1 > child 2

class A: #parent class
    a=1

class B(A): #child1 class
    b=2

class C(B):  #child2 class
    c=3

o=A()
print(o.a) # here A contains only its own attributes

o=B()
print(o.a, o.b) # here B contains att of A and B

o=C()
print(o.a, o.b, o.c) # here C contains att of A , B and C
