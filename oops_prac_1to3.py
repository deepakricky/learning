## 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:

    company= "Microsoft"
    def __init__(self, name, salary, pin):
        self.name=name
        self.salary=salary
        self.pin=pin

employee1=Programmer("Deepak",50000,501218)
print(employee1.name,employee1.salary,employee1.pin,employee1.company)

employee2=Programmer("Ash",65000,500111)
print(employee2.name,employee2.salary,employee2.pin,employee2.company)

## 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
    
a=Calculator(4)
a.square()
a.cube()
a.squareroot()

## 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’.
# Does this change the class attribute?

class Demo:
    a=5
o=Demo()
print(o.a) #print class attr cause inst att not present

o.a=0 # instance att is set

print(o.a) # prints inst att because inst att is set
print(Demo.a) #prints class att

