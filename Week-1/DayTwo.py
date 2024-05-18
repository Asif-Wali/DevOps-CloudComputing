#Lecture 2
'''Data Types in Python

'''

x=5 # this is a int data type
print(type(x))#Output will be <class 'int'>
price=36.5 #this is a float data type
print(type(price))#Output will be <class 'float'>
num=3e6 # This e will denote the exponentiation of the number.
print(num) #Output will be 3000000.0
print(type(num)) #Output will be <class 'float'>
z=4+5j
print(z) # Output will be (4+5j)
print(type(z)) #Output will be <class 'complex'>


print (abs(-10)) # This will give us the absolute value of the given value. Output will be 10.

print (pow(2,3)) #This will give us the exponent value . Output will be 8.

print (round(10.6)) # This will round the value to the nearest to the . Output will be 11 in this case.
print (round(10.5)) # This will round the value to the nearest to the . Output will be 10 in this case.

nums= [9,4,5,6,2,1,8,3,3,2,49,4,4,9]
print(min(nums))
print(max(nums))
print(sum(nums))

# Python is known for these powerful inbuilt functions.

''' Sequence types of Data '''
#1. String, To assign a string to a variable we need to wrap the value in single, double or triple quotes.
name='Asif'
my_name="Asif"
my__name='''Asif'''

# Every Alphabet inside the String has an index attached to it. and we can access it directly using variableName[positionalIndex];

print(name[2])

# Python also has something called negative indexing. We can access it from the extreme right. Its index starts from -1 and while moving towards the left the value decreases

# Strings are generally immutable across all the programming languages.  .

# str='asif'
# str[0]="w" This will throw an error because strings are immutable.

# String Concatenation

firstName="Mohammad"
LastName="Asif"

FullName=firstName+" "+LastName

print(FullName)

#Length of a string.

print(len(FullName))

# String Manipulation
# 1. String Slicing

country="United States of America"

print(country[17:24]) # Will give out the string from 17th index to 24  index
print(country[7:])# Will give out  string from 7th index till the end .
print(country[:6])# Will give out string from 0 till 8 index
print(country[:]) # Will give out whole string

# similarly we can slice using the negative index as well

School="PW Skills    "
print(School.upper()) # makes all letters uppercase

print(School.lower()) # makes all letters lowercase

print(School.capitalize()) # makes first letter capital

print(School.strip())# removes the space from left and right

# replace method.

sentence="We are currently learning DevOps and We are also learning Cloud Computing and We are learning System Design and We are learning Backend Development"
print(sentence.replace("We are", "I am" , 3))


#Escape Character 
print("Mohammmad\nAsif") #this is an escape character to print the remaining string to the new line.
print("Mohammmad\tAsif") #this is an escape character which adds a space of one tab to the string.

print("Mohammmad \"Asif\"") #this is an escape character which is used to add  inverted commas to the string.


#2 List Data Type
'''
List is a collection of elements. We can add multiple data types inside the list but it is not recommended. It is indexed and is mutable.
In Python there is nothing like Array but under the hood it is using Array Data Type.
'''
Students=["Asif", "Adil", "Anas", "Faisal", "Javaid", "Ishfaq"]

print(Students)
print(type(Students))# output will be <class 'list'>

List2=list(Students)

print(List2)
# This is the way of creating a list of students using Constructor methods.

list3=list("Mohammad")
print(list3)
# Every Alphabet of the String will be seperately placed inside the list.This is also using the constructor method.

list4= list((1,2,3,4,5))
print(list4)


#accessing the elements of the list.
Stu=["Asif", "Adil", "Anas", "Faisal", "Javaid", "Ishfaq"]
print(Stu[3])
print(Stu[-4])
# using index as well as negative index.

arr=[3,2,1,5,9]
arr.append(11)
print(arr)

# it adds the value 11 to the last of the list.

arr.insert(3,43)
print(arr)
# it will add the value of 43 at the third index.
Stu.extend(arr)
print(Stu)

#Remove Element from the List.
arrr=[1,2,3,4,5,6,7,8,9,10]

arrr.remove(9) # this will remove the element from the list but if there are more than one elements of the same value it will remove the only first element.
print(arrr)

arrr.pop() # remove the last element from the list 
print(arrr)
arrr.pop(2) # remove the third element from the list
print(arrr)

# replacing and changing the list 

list5=["a", "b", "c", "d"]

list5[2]="W"
print(list5)

Expenses=["a", "b", "c", "d", "e", "f"]

Expenses[1:4]="F", "G","H"
print(Expenses)

Expenses2=["a", "b", "c", "d", "e", "f"]

Expenses2[1:4]="F", "G"
print(Expenses2)


Expenses3=["a", "b", "c", "d", "e", "f"]
Expenses3.reverse()
print(Expenses3)

Expenses3_Copy=Expenses3.copy()
print(Expenses3_Copy)

#copy method is used to copy the list and it creates a  differentobject with a seperate id in the memory

# There is another method called sort method which actually sorts the given list

Expenses4=["d", "e", "f", "a", "b", "c" ]
Expenses4.sort()
print(Expenses4)


#3 Tuple Data Type

'''
1.This is an ordered Data Type
2. This is a sequencial Data Type
3. This is immutable Data Type
4.Can accomodate different types of Data
5.index also starts from Zero.0
# Immutability is the unique feature of this Data Type
'''

Tuple1=(1,2,3,4,5)
print (Tuple1)

print(type(Tuple1))

Tuple2=tuple(Tuple1)
# Tuple can be created using constructor function also by using list or string or directly hardcoding tuple . It is generally enclosed inside round brackets

t=(35)
print(type(t))
# it will give out type of t as the int instead of tuple to make python consider it as tuple we have to add a comma "," at the end .

fruits=("apple", "orange", "apple", "mango", "orange", "apple","Strawberry")
print(fruits.count("apple"))
print(fruits.count('apple'))
print(fruits.count("jackfruit"))

print(fruits.index("apple"))

# Tuple is immutable we cant assign any new value but we can do slicing operation on tuple


#4 Boolean Data Type

'''
True and False
'''
#5 Dictionary Data Type

'''
1. This is an unordered Data Type
2. This is a sequencial Data Type
3. This is mutable Data Type
4. Data is stored in key/value pairs.
5. Can accomodata heterogeneous data types
6. Key Should be unique
7. index also starts from Zero.0  
'''
Student_Details={'name': 'Asif', 'age':21 , 'city':'Srinagar'}
print(type(Student_Details))


dict1={1:'Asif',2:"Wali", True: "Ganai"}
print(dict1)
# It outputs 1: Ganai, the reason it happens is that the python reads True as 1 and False as 0 so when the code is compiled we have two keys by the name of 1 so the last one overrides the first key. therefore the end result.



dict_2= dict(name="asif", age=23, )
#While using constructore method we can't use reserved keywords.

print(dict_2)




dict2={'name': 'Asif', 'age':21 , 'city':'Srinagar'}
print(dict2['name'])
print(dict2['age'])
print(dict2['city'])
# we can access the values of the dictionary by using the key.


print(dict2.keys())
print(dict2.values())

# to add the entry to the dictionary

dict2['State']="Kashmir"
print(dict2)

# to merge the two dictionaries into one

dict3={'name': 'Asif', 'age':21 , 'city':'Srinagar' , 'institution':'PWSkills' , 'Bootcamp':'Masai School'}
dict4={'name': 'Adil', 'age':22 , 'city':'Srinagar'}
dict3.update(dict4)
print(dict3)

# to delete the entry from the dictionary

del dict3['age']
print(dict3)

dict3.pop('name')

print(dict3)

dict3.popitem()

print(dict3)

dict3.clear()

print(dict3)
# clear method is used to empty the dictionary;

#6 Set Data Type 
'''
1.Mutable;
2.Unordered;
3.Uniqueness/ No Duplicates;
4. Heterogenous;
'''

set1={1,2,3,4,5}
print(type(set1))
# output <class 'set'>

set2=set({789,786,5,165,547})
print(set2)

set3={1,2,3,4,5,1,5,9,1,6,45,8,1}

print(set3)

#  to add to the set
set3.add(99)
print(set3)

set3.discard(99)

print(set3)

# 7. Frozen Set Immutable set.

frozenset1={1,2,3,4,5}
print(type(frozenset1))

frozenset2=frozenset({789,786,5,165,547})

print(frozenset2)

frozenset3=frozenset(frozenset1)
print(frozenset3)

# frozenset3.add(99) This will throw an error because frozen set in immutable.


'''
TypeCasting
1.implicit type casting
2.explicit type casting
'''
#Implicit Type Casting
x=5
print(type(x))
y=6.5
print(type(y))
result=x+y
print(result)
print(type(result))
# This type of casint is done by python compiler itself where an int after operation becomes a float data type.

#Explicit Typecasting
a="10"
print(type(a))
b=int(a)
print(type(b))

# This type of casting is done by the programmer where using an inbuilt method we changed the type of a varibale from str to int.

'''
Some inbuilt methods for type casting
int()
str()
float()
and others
'''



