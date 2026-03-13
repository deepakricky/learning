#class
class Employee:
    language="py" # This is a class attribute
    salary= 10000
#object
deepak=Employee()
deepak.name="Deepak" # This is an object/instance attribute
print(deepak.name, deepak.language,deepak.salary)

batman=Employee()
batman.name="Batman Dk"
print(batman.name, batman.language,batman.salary)

# Here name is instance(object) attribute and salary and language are class attributes as they directly belong to the class
