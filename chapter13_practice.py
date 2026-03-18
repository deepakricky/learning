## Write a program to filter a list of numbers which are divisible by 5.
def divisible(n):
    if (n%5==0):
        return True
    return False
a= [2,5,22,2424,125325,62455,55,65,230]
f=list(filter(divisible,a))
print(f)

## Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
a= [2,5,22,24,125,65,59,230]
def greater(a,b):
    if a>b:
        return a
    return b
print(reduce(greater,a))
