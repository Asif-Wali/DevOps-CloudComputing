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




