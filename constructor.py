class Employee:
    
    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

deepak=Employee("Deepak", 50000, "Python")
print(deepak.name,deepak.salary,deepak.language)
