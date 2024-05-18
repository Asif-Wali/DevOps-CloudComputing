# Conditionals in Python

"""
if condition:
   statement
elif condition:
   statement
else:
   statement
"""

x = 10
if x > 9:
    print("x is greater than 9")

# This is the if condition which is followed by expression if that expression is true then the indented code block will run

x = 10
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")

# This is the  if else condition which is followed by expression if that expression is trie  then the if block will run otherwise else block will run.   


x = int( input("Please Enter a number "))

if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10")

# This is the if elif else condition which is followed by expression if that expression is true then the if block will run otherwise elif block will run otherwise else block will run.


# After this we studied Truthy value and Falsy Value


# Nested if Else conditions, Multiple levels of conditionals are allowed in Python language.

num=5

if num > 0:
    print("Number is positive")
    if num > 10:
        print("Number is greater than 10")
    else:
        print("Number is less than 10")
else:
    print("Number is negative")
 


# Ternary operators in Python

x = 10
y = 20 if x > 10 else 30
print(y)

# Instead of Switch Statements Python has Match and Case statements in Python
 

x = 99
match x:
    case 10:
        print("x is 10")
    case 20:
        print("x is 20")
    case 30:
        print("x is 30")
    case 40:
        print("x is 40")
    case 50:
        print("x is 50")
    case 60:
        print("x is 60") 
    case _:
        print("Doesn't Match any Condition")                   