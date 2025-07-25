# FOR LOOPS = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# Basic Iteration
fruits = ['apple', 'banana', 'kiwi', 'pear']

for fruit in fruits:
    print(fruit)

# Sequences that we can loop through:

# strings
for char in 'Harry':
    print(char)

# list: example above (fruits)

# tuples and sets
languages = ('EN', 'PT', 'ES', 'FR')
for lang in languages:
    print(lang)

# range() 
# can put start, stop, step - mandatory is start
# stop point is not included 

# prints hello + i (number) it starts from 1 - prints odd numbers 
for i in range(1,11,2):
    print('hello', i)

# this WON'T WORK if you don't put range - an int is not iterable
# for i in 10:
#     print(i)

# Iterate backwards - reversed + range
for x in reversed(range(1, 11)):
    print(x)

# enumerate - like range but it returns index + element
# good for when you want to manipulate very long lists 

for i, fruit in enumerate(fruits):
    if fruit == 'apple':
        fruits[i] = 'Windows is better'
    else:
        print(f'Fruit {i} is {fruit}')

print(fruits) 

# continue - skips over an iteration
for x in range(1, 21):
    if x == 13:
        continue # doesn't print 13 but continues to 14 and so on...
    else:
        print(x)

# break - breaks out of the loop entirely 
for x in range(1, 21):
    if x == 13:
        break # breaks out of loop, prints until 12 and stops
    else:
        print(x)


# NESTED LOOP = A loop within another loop (outer, iner)
#               outer loop:
#                   inner loop:

# execute the code that prints numbers 1-10 - 3 times
for x in range (3):
    for y in range(1, 10):
        print(y, end="") # this prints all the numbers on the same line instead of one below the other


# Exercise - accept a number from the user and print its multiplication table
user_number = int(input("Enter a number: "))
for num in range(0,11):
    print(f"{user_number}*{num}= {user_number * num}")

# WHILE LOOP = execute some code WHILE some condition remains true

# example 1
name = input("Enter your name: ")

while name == "": # while this remains true, keep asking for user's name
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}") 

# example 2 - while not
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")

# Exercise - Print the numbers from 1 to 10 using while loop

number = 1
while number < 11:
    print(number)
    number += 1

# while loop with break
while True:
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        break
    else:
        print("I'd love to go to ", city)

print("Goodbye!")

# continue - returns to the beginning of the loop (skips the rest of the iteration)
current_number = 0
while current_number <= 10:
    current_number += 1 
    if 3 < current_number < 7:
        continue # go back to the beginning of the loop 
    print(current_number)


# WHILE LOOP: Used to execute a block of code an unknown amount of times 
#             until a certain condition is True / until there is a "break" keyword

# counter is called "i" for "iteration"