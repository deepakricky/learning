class Employee: #Base class(Parent class)
    company= "ITC"
    name="Deepak"
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

class Programmer(Employee): #child class
    company= "ITC infotech"
    language="Python"
    def showLanguage(self):
        print(f"The name is {self.name} and he knows {self.language} language")

a=Programmer()
print(a.company)
print(a.name) # here we can see im printing name from child class which was first in parent class
