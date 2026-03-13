#Function definition
# def avg():
#     a=int(input("Enter number: "))
#     b=int(input("Enter number: "))
#     c=int(input("Enter number: "))
    
#     print(f"The average is {(a+b+c)/3}")

# avg() #function call
# print("Thank you!")
# avg()
# avg()

## Write a program to greet a user with “Good day” using functions.
# def gd():
#     print("good day")

# gd()

## Functions with arguments

# def gd(name,ending):

#     print("Good day, "+name,)
#     print(ending,"\n")

#     return "Done"

# a= gd("Zoro","Thanks buddy")

# print(a)

## default parameters
def chips(name="Lays"):

    a=print(f"{name} is very good")
    return a

chips() # Here it is taking default value that we have given, which is Lays
chips("Bingo")
