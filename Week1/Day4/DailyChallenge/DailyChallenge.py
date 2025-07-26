# Challenge 1: Multiples Of A Number

number_input = int(input("Choose the number you want me to multiply: "))
length_input = int(input("Choose a number so I know how many times to multiply it: "))
multiples = []

for num in range(length_input):
    multiples.append(number_input * (num + 1))

print(multiples)


# Challenge 2: Remove Consecutive Duplicate Letters

word = input("Write a word: ")

unique_string = ""

for index in range(len(word)):
    if index == 0 or word[index] != word[index-1]:
        new_string += word[index]

print(unique_string)