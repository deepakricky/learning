## 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The 2D vector is {self.i}i + {self.j}j")

class ThreeDvector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")

a= TwoDVector(1,2)
a.show()

b=ThreeDvector(1,2,3)
b.show()

## 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow")

a=Dog()
a.bark()

## 3. Create a class ‘Employee’ and add salary and increment properties to it.
##Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.
class Employee:
    salary = 234
    increment = 20 
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter 
    def salaryAfterIncrement(self, salary):
        self.increment =  ((salary/self.salary) -1)*100 




e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.increment)
