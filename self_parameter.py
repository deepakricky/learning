class Employee:
    language= "Python" #class attribute
    salary= 20000

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    def greet(self):
        print("Good morning")
    
deepak=Employee()
deepak.language="Java" #instance attribute
deepak.greet()
deepak.getInfo()
# Employee.getInfo(deepak)
