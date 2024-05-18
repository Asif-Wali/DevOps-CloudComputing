# Operators in Python.
'''
There are four Types of Operators in Python.
1. Arithmetic Operators
2. Comparison Operators 
3. Logical Operators
4. Assignment Operators
5. Bitwise Operators
6.Membership Operators
7. Identity Operators

'''


#1. Arithmetic Operators

num1=10
num2=20

print(num1+num2) # Addition Operators

print(num1-num2) # Subtraction Operators

print(num1*num2) # Multiplication Operators

print(num1/num2) # Division Operators , Ouput will be a float value;

print(num1//num2) # Floor Division Operators, Ouput will be an integer value;

print(num1%num2) # Modulus Operators, It will output  the remainder of the division;

print(num1**num2) # Exponentiation Operators, It will output the power of the number;

# There is something called Positive and Negative Infinity in python 

pos_int= float("inf")

print(pos_int)

neg_int= float("-inf")

print(neg_int)


# There is also a special NAN operator which is used to represent Not a Number

nan= float("nan")
print(nan)


#2. Comparison Operators
num3=30
num4=40

print(num3==num4) # Equality to Operators

print(num3!=num4) # Not Equal to Operators

print(num3>num4) # Greater than Operators

print(num3<num4) # Less than Operators

print(num3>=num4) # Greater than or Equal to Operators

print(num3<=num4) # Less than or Equal to Operators

# NAN is consistently unequal to any other value

#3. Assignment Operator

num5=50 #  Assigning a value to a variable
num5+=6 # Increment and Assign


num5-=6 # Decrement and Assign

num5*=6 # Multiplication and Assign

num5/=6 # Division and Assign

num5//=6 # Floor Division and Assign

# 4.Logical Operators

print(True and True) # Logical AND Operator, Will Print True because Logical AND operator checks for both the values to be true. 

print(True and False) # Logical AND Operator,  Will Print False because Logical AND operator checks for both the values to be true. 

print(True or False) # Logical OR Operator, Will Print True because Logical OR operator checks for only single value to be true.

print(False or False) # Logical OR Operator, Will Print False because both the values are false.

print(not True) # Logical NOT Operator, Will Print False because Logical NOT operator gives opposite value of True in this case,

print(not 5>7) # Logical NOT Operator, Will Print True because Logical NOT operator gives opposite value of False in this case,

# Xor operator

print(True ^ True) # Logical XOR Operator, Will Print False  because Logical XOR operator checks for  both values to be unequal.

print(True ^ False) # Logical XOR Operator, Will print True because in this case there are two different values.

print(False ^ False) # Logical XOR Operator, Will Print False because both the values are same.

# 5. Bitwise Operators

num6=5
num7=3

print(num6&num7) # Bitwise AND Operator, Will Print 1 because in this case the values will be 101 & 011 in Binary and when we try to compare the values it will be 001. therefore 1;

print(num6|num7) # Bitwise OR Operator, Will Print 7 because in this case the values will be again 101 & 011 in Binary and when we try to compare we get 111 and by changing it to decimal we get 7.

print(num6<<1) # This operator is a bitwise left shift operator. It shifts the bits of a number to the left by the specified number of positions. It Doubles the value of the Decimal number.

print(num6>>1) # This operator is a bitwise right shift operator. It shifts the bits of a number to the right by the specified number of positions. It halves the value of the  Decimal number.

# 6. Identity Operator

num8=5
num9=5
print(num8 is num9) # This operator is identity operator, It is used to check the identity whether the two variable are pointing to the same object in memory.

print(num8 is not num9) # This operator is identity operator, It is used to check the identity whether the two variable are not pointing to the same object in memory.

# 7. Membership Operator

list1=[1,2,3,4,5]
print(1 in list1) # This operator is membership operator, It is used to check whether the value is present in the list or not.

print(1 not in list1) # This operator is membership operator, It is used to check whether the value is not present in the list or not.


