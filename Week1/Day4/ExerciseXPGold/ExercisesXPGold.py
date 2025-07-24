import random

# # Exercise 1: Concatenate Lists
fruits = ['banana', 'strawberry', 'mango', 'coconut']
vegetables = ['tomato', 'cucumber', 'pepper', 'carrot']
fruits.extend(vegetables)
print(fruits)

# Exercise 2: Range of Numbers
for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)


# Exercise 3: Check The Index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name_input = input('What\'s your name?: ')
for name in names:
    if name == user_name_input:
        print(names.index(name))
        break 


# Exercise 4: Greatest Number
numbers = []

# Ask user to input 3 numbers

num_1 = int(input("Input the 1st number: "))
num_2 = int(input("Input the 2nd number: "))
num_3 = int(input("Input the 3rd number: "))

numbers_input = [num_1, num_2, num_3]

# Return max number
print(f'The greates number is: {max(numbers_input)}')


# Exercise 5: The Alphabet
vowels = ('a', 'e', 'i', 'o', 'u')
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
    if letter in vowels:
        print(f'{letter} is a vowel!')
    else:
        print(f'{letter} is a consonant!')
    

# Exercise 6: Words and Letters

words_input = input("Type up to 7 words separated by spaces: ")
words = words_input.split(" ")

letter = input('Type a single letter from the english alphabet: ')

for word in words:
    if letter in word:
        print(word.index(letter))
    elif letter not in word: 
        print(f'The letter {letter} is not in {word}')
        

# Exercise 7: Min, Max, Sum

one_to_million = [num for num in range(0, 1000001)]
print(min(one_to_million))
print(max(one_to_million))
print(sum(one_to_million))


# Exercise 8: List and Tuple

number_sequence = input("Enter a sequence of comma-separated numbers: ")
sequence_list = number_sequence.split(',')
sequence_tuple = tuple(sequence_list)
print(sequence_list)
print(sequence_tuple)


# Exercise 9: Random Number 

won_counter = 0
lost_counter = 0

while True:
    # ask user to enter a number
    user_input = input("Enter a number from 1-9 (write 'quit' to exit): ")
    random_number = random.randrange(1,9)
    # check if user wants to quit and exit loop
    if user_input.lower() == 'quit':
        break
    # transform input into integer 
    elif int(user_input) not in range(1,10):
        print("You've entered an invalid number")
    else:
        user_input = int(user_input)
        if user_input == random_number:
            print('Winner')
            won_counter += 1
        else:
            print(f'The number was {random_number}, better luck next time')
            lost_counter += 1


print(f'Total games won: {won_counter}\nTotal games lost: {lost_counter}')

