class Employee: #Base class(Parent class)
    company= "ITC"
    
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

class Programmer(Employee): #child class
    company="ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he knows {self.language} language")

a=Programmer()

print(a.company)
