# Lecture 1
# Python is a programming language. Programming languages are of two types: 1. Compiled(Java, C++) and 2. Interpreted(Python).
# The Programming language code is first compiled where it checks that the syntax is correct and error free. After compilation the code is then translated to Byte Code and then it is finally executed. This is the case of Compiled Language.
# The programming language where the code is checked line by line and executed simultaneously without any syntatical check is called Interpreted language. Interpreted Programming language is slow as compared to compiled type programming language.

'''
Python is interpreted language. It is dynamically typed language. It is case sensitive.
'''



'''
Why Python ? 
1.Python is versatile and is used in Data Science, AI, ML. 
2.The Python language is very easy to understand.
3. It is used in so many domains like Development, Scripting
'''

'''
How to use Python?
First in order to run any programming language you need a run time environment. Eg for Java we need Java Runtime Environment, for JavaScript we need Node.js. Similarly for Python we need to install python to run our python code.
And we can do that by downloading and installing Python from official website. Additionally we need to install IDE(Integrated Development Environment) to write the  code. 
'''


print("My name is Asif and I am learning Python for DevOps and Cloud Computing")


# Variables are usually defined  as  container to store data. There are two types of variables one is  Dynamically typed and another is statically typed variable. Statically typed variables are where we are required to intitalize what type of data will the variable store, while dynamically typed variables are those where we just  need to declare a variable and the programming language handles the rest.

# While naming a variable you can use alphabets which can be uppercase or lowercase or underscore but the variable name shouldn't have any special character like % sign or Dollar sign.
# Variable names are case sensitive ie. uppercase and lowercase are different variable .
# We cant keep reserved keywords as our variable names it'll throw an error.
# Variable name should be a single word python doesn't support having a space between two words as your variable name, instead we can use underscore
# Variable name should be relevant name.

x=5
'''
In the above statement, the x is the name of the variable and 5 is the value, so x is pointing to the memory location which holds the object of 5. X is also called as the reference of the object in memory. 
'''
name='Asif'
age=99
print(id(age))
x=99
print(id(x))

'''
In the above example, if you notice the output of the code you will notice that id of both variables i.e; age and x is same which confirms that the value 99 has two references and the id is actually the memory location of the value in the computer memory.
'''

'''How to add comment to our code in python
1.To add a single line comment we can use a # in the starting of the line which will tell python to ignore the line and move to another line.
2. To add a multi line type we can use triple quotes between lines. Anything written between the three lines will be ignored by Python.
'''



# Taking input from the user.
#Input function is an inbuild function in Python which is used to take input from the user.
#Every Input that we read from User is treated as a string.

# My_Name=input()
# print(My_Name)

# age=input("Please sir, Enter your age in years  ")
# print(age)

# Ourput in the world of Python.

friend_name="Mohammad Asif"
friends_age=26

print("Hello, my friends name is",friend_name,"and his age is",friends_age)

# Support for formatted string.

print(f"Hello, my friends name is {friend_name} and his age is {friends_age}")

a=1 
y=2
z=3
print(a,y,z, sep="%")

# In the above snippet the sep keyword will seperate the values of a, y, and z by the written value. 

print("Hello")
print("world!")
print("How are you?")

# They will all print the values in next line.

print("Hello", end=" ")
print("world!", end=" ")
print("How are you?", end=" ")


