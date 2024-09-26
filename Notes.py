'''
    Lesson: Boolean Logic
    Author: Mr. Kalisz
    Date Created: Sept 26, 2024
    Date Last Modified: Sept 26, 2024
'''

#Review

bool1 = 5 > 3
#bool1 = True

#And

print(True and False)

#Or

print(True or False)

#Not

print(not False)

#DONT DO THIS

num = 3

#Is this number positive and less than five
#print(0 < num < 5)
#True < 5

#how to fix this - on either side of "and" or "or", you need to have a boolean

print(num > 0 and num < 5)

print(False and False or True)
#False or True
#True

print(True or False and False) #True due to Order of Operations

print(not True and False or not True and False)
#False and False or False and False

print(True or not False and not True and False or not True and False or True)
#Any boolean expression that start with "True or" or "or True" is always true

print((True or False) and False) # False
#True and False
#False

print(not(not(not(not(True))))) #True
#two nots cancel each other out

#DO NOT DO THIS

word = "Computer"

print(word == "robot" or "Hello")
#False or "Hello"

print(word == "robot" and "Hello")
#True or "Hello"