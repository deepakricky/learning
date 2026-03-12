## Write a program to print multiplication table of a given number using for loop.
# num=int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

## Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")

##Attempt problem 1 using while loop.
# n=int(input("Enter num: "))
# i=1
# while(i<11):
#     print(f"{n} x {i} = {n*i}")
#     i+=1

##Write a program to find whether a given number is prime or not.
# n=int(input("Enter num: "))
# for i in range(2,n):
#     if(n%i==0):
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

##Write a program to find the sum of first n natural numbers using while loop.
# n=int(input("Enter number: "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i #going from 1 to n
#     i+=1
# print(sum)

##Write a program to calculate the factorial of a given number using for loop.
##The factorial of a non-negative integer (denoted as ) is the product of all positive integers less than or equal to .
# n=int(input("Enter number: "))
# product=1
# for i in range(1,n+1):
#     product=product*i
# print(f"factorial of {n} is {product}")

##star pattern

##1
# n=int(input("Enter number: "))
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1),end="")
#     print("")

##2
# n=int(input("Enter number: "))
# for i in range(1,n+1):
#     print("*"*i,end="")
#     print("")

##3
# n=int(input("Enter number: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")

## Write a program to print multiplication table of n using for loops in reversed order.
n=int(input("Enter number: "))
for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")
