#Loops
# 1. For Loops
# 2. while loops

# To run a For loop we need a sequencial data.

fruits= ["apple","orange","banana","mango", "Strawberry", "blackberry", "jackfruit"]

for fruit in fruits:
    print(fruit)

name="Mohammad Asif"

for letter in name:
    print(letter, end=" ")


for i in range(10):
    print(i)

# This will run from 0 to 9  
for i in range(6,12):
    print(i)

# This will run from 6 to 11 with a step of 1 which is the default value unless specified otherwise 

for i in range(6,12,2):
    print(i )

# This will run from 6 to 12 with a step of 2.

for i in range(12,6,-1):
    print(i)

# This will run in reverse order.

# Controlling the flow of the loops

for i in range(10):
    if i==5:
        break
    print(i)

# Break keyword will remove you from the loop

for i in range(10):
    if i==5:
        continue
    print(i)

# Continue keyword will skip the current iteration of the loop.


# Nested Loops

for i in range(3):
    for j in range(3):
        print(i,j)

# While loops

i=0
while i<10:
    print(i)
    i=i+1

    

