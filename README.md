Module :
Module is a file containing code written by somebody else (usually) which can be imported and used in our programs
PIP:
Pip is the package manager for python. You can use pip to install a module on your system

REPL: Read Evaluate Print Loop

Rules for choosig an identifier
A variable name can contain alphabets, digits, and underscores.
A variable name can only start with an alphabet and underscores.
A variable name can’t start with a digit.
No while space is allowed to be used inside a variable name.

input: It is important to note that the output of input is always a string (even is a number is entered). to take input as int for example : a=int(input("number:"))

String is a data type in python.
String is a sequence of characters enclosed in quotes.
Strings are immutable which means that you cannot change them by running functions on them


ESCAPE SEQUENCE CHARACTERS
Sequence of characters after backslash "\" → Escape Sequence characters
Escape Sequence characters comprise of more than one character but represent one character when used within the strings.

Lists: Python lists are containers to store a set of values of any data type.
lists are mutable

A tuple is an immutable data type in python.

Dictionary is a collection of keys-value pairs.
1.It is unordered.
2.It is mutable.
3.It is indexed.
4.Cannot contain duplicate keys.

Set is a collection of non-repetitive elements.
1.Sets are unordered => Element’s order doesn’t matter
2.Sets are unindexed => Cannot access elements by index
3.There is no way to change items in sets.
4.Sets cannot contain duplicate values.

Condtional exp, if else and elif:
1.There can be any number of elif statements.
2.Last else is executed only if all the conditions inside elifs fail.

Loops:

Sometimes we want to repeat a set of statements in our program. For instance: Print 1 to 1000.
Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how!

Primarily there are two types of loops in python.
•while loops
•for loops

while loop:

In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed otherwise not!
If the loop is entered, the process of [condition check & execution] is continued until the condition becomes False.

for loop:

A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

range fucntion:

The range() function in python is used to generate a sequence of number.
We can also specify the start, stop and step-size as follows: range(start, stop, step_size) # step_size is usually not used with range()

FOR LOOP WITH ELSE: 
An optional else can be used with a for loop if the code is to be executed when the loops exhausts.

THE BREAK STATEMENT: 
‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now.

THE CONTINUE STATEMENT
‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.

PASS STATEMENT
pass is a null statement in python.
It instructs to “do nothing”.

FUNCTIONS & RECURSIONS:

A function is a group of statements performing a specific task.
When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!
A function can be reused by the programmer in a given program any number of

The syntax of a function looks as follows: 
def func1():
    print('hello')
    
This function can be called any number of times, anywhere in the program.

FUNCTION CALL: 

Whenever we want to call a function, we put the name of the function followed by parentheses as follows: func1() # This is called function call.

FUNCTION DEFINITION:

The part containing the exact set of instructions which are executed during the function call.

TYPES OF FUNCTIONS IN PYTHON

There are two types of functions in python:

•Built in functions (Already present in python)

•User defined functions (Defined by the user)

Examples of built in functions includes len(), print(), range() etc.

The func1() function we defined is an example of user defined function.
