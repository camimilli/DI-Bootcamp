# BASIC VALUE TYPES

# general info:
# comments = # or Ctrl + /

# -STRINGS
# text, sequence of characters, defined with quotations marks: '' OR ""

'Hello World'

# -Variables: like "boxes" where we can store data types (info)

greeting = 'Hello World'

# print() = A function that "prints" something to the console

# -STRING METHODS = are functions that we can apply into strings
print(greeting.capitalize())
print(greeting.upper())
print(greeting.lower())

# string indexing
print(greeting[3])

# string slicing 
print(greeting[1:8])

#Exercise 1
description = "strings are..."

print(description.upper())
print(description[:7])
print(description.replace('are', 'is'))


# - NUMBERS
# - INTEGER = WHOLE NUMBER (NO DECIMAL)
# - FLOATS = DECIMALS
# - COMPLEX NUMBERS = NUMBERS + LETTERS

my_fav_num = 7
print(type(my_fav_num)) #int

my_high = 1.59
print(type(my_high))

#MATH OPERATIONS WITH NUMBERS 

print(5 + 3)
print(5 - 3)
print(5 - 7)
print(5 - (-3))
print(5 * 3)
print(15/3)
print(15/4)
print(15//4)
print(11%2)

#Math with string
#obs.: \n is a special character that create a new line
print('Juliana \n' * 5)
print('Juliana' + 'Schmidt')

#COMPARISON OPERATORS 

print(3 > 4) #False
print(3 < 4)
print(3 <= 4)
print(3 <= 3)
print(3 >= 3)
print(3 == '3')
print(3 == 5)

#Type Casting

age = '35'
print(int(age) + 123879)
print(age + str(123879))

#BOOLEANS:True and False