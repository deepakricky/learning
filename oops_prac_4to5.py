## 4. Add a static method in problem 2, to greet the user with hello.
class Calculator:
    
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
    
    @staticmethod
    def greet():
        print("Hello")

a=Calculator(4)
a.greet()
a.square()
a.cube()
a.squareroot()

## 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo=trainNo
    
    def book(self, fro, to):
        print(f"Ticket is booked in train num {self.trainNo} from {fro} to {to} ")

    def getStatus(self):
        print(f"Train no. {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"The fare for train num {self.trainNo} from {fro} to {to} is: {randint(111,555)}")

a=Train(225589)
a.book("Hyderabad","Delhi")
a.getStatus()
a.getFare("Hyderabad","Delhi")
