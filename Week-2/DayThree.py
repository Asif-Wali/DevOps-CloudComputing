# Functions in Python
'''
Function is a block of code that can be reused multiple times.

'''
# Keyword def is used to define a function in Python.
def firstfunction(): # This is function definition
    print("This is my first function")

firstfunction() # This is function invocation.

def add(a,b): # This is a function which gives us back some value it is achieved 
#using return keyword. and letters a and b here are called parameters
    return a+b

print(add(10,20)) #  Here is a function invocation and the numbers 10 and 20 are arguments.


x = 10 # Global variable

def printx():
    x=20
    print(x)

print(x)
printx()

# Default value of a Parameter

def add(a,b=10):
    return a+b

print(add(10))
print(add(10,20))

#incase the user misses to add the value of second argument it will take 10 value by default.

# Keyword arguments

def add(a,b):
    return a+b

print(add(a=10,b=20))

# incase we want to change the order of the arguments we can use keyword arguments.
# we need to give keyword to all the arguments 

# Positional arguments
# we have to follow the order of the arguments in order to get the correct output.


def func(*args):
    print(type(args))
    print(args)
    sum=0
    for num in args:
        sum+=num
    return sum     

# This is a function declaration where we dont no the number of arguments or variable number of arguments.


def sum_of_number(a,b, *args):
    print(a)
    print(b)
    print(args)
    print(*args)

sum_of_number(7,8,9 ,10,11,12)


def sum_of_number2(*args,a,b):
    print(a)
    print(b)
    print(args)
    print(*args)

sum_of_number2(7,8,9 ,10,a=11, b=12)

#This will throw an error because all the arguments will be assigned to *args
#One thing to tackle this is that to keep the *args parameter at the last of use keyword arguments

#kwargs

def func(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
     print(key, "->", value)    

func(a=10,b=20,c=30,d=40,e=50)

def func2(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
func2(5,6,7,8,9, name="Asif", age="27")

# def func3(**kwargs,a,b): #This will throw an error.
#     print(a)
#     print(b)
#     print(kwargs)

# func3(name="Asif", age="27", city="Srinagar",7,9)

# This will through an error because kwars should  always be placed at the last of the function declaration

def returnType(a:int, b:int )->int:
    return a+b

print(returnType(10.5,20.5))

#Nested functions

def outer():
    print("This is outer function")
    def inner():
        print("This is inner function")
    return inner

nestedfunction=outer() # This will print  the "This is outer function" and then will return the inner function because of return keyword and store it inside the variable

nestedfunction() # In the previous line this variable received the inner function and on this line we are calling that inner function and this will print the "This is inner function" 

print(nestedfunction) # This is printing this -> "<function outer.<locals>.inner at 0x0000013261129760>" 

outer()() #This line will directly call the function inside the outer function i.e inner function will be called.



#Pass by Value in Python

# An argument is passed by two ways in a function , 
'''
1. Pass by value:-> Pass by value means where we send the copy of the value and not the orignal  value
2. Pass by  reference



'''

num_1=5

def modify_num(num):
    num=num+1
    print(num)

modify_num(num_1) 

print("Original Num", num_1)

'''
In the above example we are sending the copy of the value of num_1 to the function modify_num.
In the function modify_num we are adding 1 to the value of num and printing it which will be 6.
In the last line we are printing the value of num_1 which is still 5. '''

# Pass by reference

mylist=[1,2,3,4]
def modiyList(li):
    li.append(5)
    print(li)
print("Before Calling Fun", mylist)

modiyList(mylist)

print("After Calling Fun", mylist)

'''
In the above example we are sending the the original address of mylist to the function modiyList.
In the function modiyList we are appending 5 to the list and printing it which will be [1,2,3,4,5].
In the last line we are printing the value of mylist which is [1,2,3,4,5]. '''


# so if the Data type is immutable the Data type will be send as a value/Copy of the original but if the Data type is mutable then the value is sent as original data type and then inside the function it is changed


# Lambda Function

'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

'''

func=lambda x: x+10

print(func(10))

func2=lambda x,y: x+y

print(func2(10,20))

# Lambda function become very handy in nested functions

def outer():
        return lambda msg: print(msg)
    
outer()("Hello, World!")

# Modules and Packages

'''
Modular Programming 
is a programming technique which tells us to divide program into different files and folders to make our code simpler and easier to read

'''
import Module
Module.cube(5)

import Module as M # using alias for module.
M.cube(5)

from Module import * # it will import all the contents of this module   

cube(5)

from Module import cube # it will import only the cube function from the module.

cube(5)
#inbuilt Modules

import sys

print(sys.path)

#Package
'''
The difference between the module and the package is that the module represents one single python file while as the package represents the folder containing 
multiple python files.Usually it has --init-- file which holds the code that we want to run before the initialization of the package

'''
# from Mypackage import module1, Module2  # This is how we import the modules from package and with this we have completed our 2nd week