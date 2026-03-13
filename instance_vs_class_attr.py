class Employee:
    language= "Python" #class attribute
    salary= 50000

itachi=Employee()
itachi.language="JavaScript" #instance attribute
print(itachi.language,itachi.salary)

#Instance attributes, take preference over class attributes during assignment & retrieval.
