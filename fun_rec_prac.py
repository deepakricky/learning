## Write a program using functions to find greatest of three numbers.

def num(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a=int(input("Enter num: "))
b=int(input("Enter num: "))
c=int(input("Enter num: "))

print(f"Greatest of number is {num(a,b,c)}")

## Write a python program using function to convert Celsius to Fahrenheit.

def c_to_f(c):
    f=(9/5) * c + 32
    return f
c=float(input("Enter temp in celsius: "))
print(f"{c} C is equal to {round(c_to_f(c),2)} F") #round take only 2 decimals after . in number

# How do you prevent a python print() function to print a new line at the end.
print("a")
print("very", end="")
print("Good")
print("day")

## Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n
'''

def sum(n):

    if(n==1): #important to write
        return 1
    
    return sum(n-1) + n

n=int(input("Enter number: "))

print(f"The sum is {sum(n)}")

## star pattern in decreasing order n

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(5)

## Write a python function which converts inches to cms.
def i_to_c(i):
    c= i*2.54
    return c
i=int(input("Enter inches: "))
cen=i_to_c(i)
print(f"{i} inches is {round(cen,2)} cm")

##or simpler way

def inch_to_cm(inch):
    return inch*2.54
n=int(input("Enter inches: "))
print(f"Value in cm is {inch_to_cm(n)}")

## Write a python function to print multiplication table of a given number.

def mult(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
mult(5)
