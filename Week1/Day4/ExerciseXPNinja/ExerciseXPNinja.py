# Exercise 1: Formula
import math
import random

C = 50 
H = 30

# Ask user for numbers
user_input = input("Enter a comma-separated string of numbers: ")
numbers_string = user_input.split(",")

# Convert numbers to integers 
numbers = [int(num) for num in numbers_string]

# Apply square root to numbers 
for index, num in enumerate(numbers):
    numbers[index] = round(math.sqrt((2 * C * num)/H))
   
# print numbers
print(*numbers_string, sep=', ')


# Exercise 2: List Of Integers

numbers_1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
numbers_2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
numbers_3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
numbers_4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# 1
all_numbers = numbers_1 + numbers_2 + numbers_3 + numbers_4

# 2a 
print(all_numbers)

# 2b
all_numbers_sorted_reverse = sorted(all_numbers, reverse=True)
print(all_numbers_sorted_reverse)

# 2c 
print(sum(all_numbers))

# 3
first_and_last = [all_numbers[0], all_numbers[-1]]
print(first_and_last)

# 4 
greater_than_50 = list((num for num in all_numbers if num > 50))
print(greater_than_50)

# 5
smaller_than_10 = list(num for num in all_numbers if num < 10)
print(smaller_than_10)

# 6 
squared_numbers = list(round(math.sqrt(num)) for num in all_numbers if num > 0)
print(squared_numbers)

# 7
all_numbers_no_duplicates = set(all_numbers)
all_numbers_no_duplicates = list(all_numbers_no_duplicates)
print(all_numbers_no_duplicates)

# 8
average = round(sum(all_numbers) / len(all_numbers))
print(average)

# 9
print(max(all_numbers))

# 10
print(min(all_numbers))

# 11
# sum 
sum_numbers = 0

for num in all_numbers:
    sum_numbers += num

print(sum_numbers)

# average 
average_result = round(sum_numbers / len(all_numbers))
print(average_result)

# largest number

largest_num = all_numbers[0]

for num in all_numbers:
    if num > largest_num:
        largest_num = num
        
print(largest_num)

# smallest number

smallest_number = all_numbers[0]

for num in all_numbers:
    if num < smallest_number:
        smallest_number = num
        
print(smallest_number)

# 12 

ten_numbers = []
i = 0
numbers_left = 10

while i != 10: 
    user_input = int(input(f"Enter a number in range -100 to 100, you have {numbers_left} numbers left: "))
    if user_input > 100 or user_input < -100:
        print(f'You entered {user_input}, this is not a number between -100 and 100, try again, you have {numbers_left} numbers left: ')
    else:
        ten_numbers.append(user_input)
        i += 1 
        numbers_left -= 1

print(f'These are the numbers you chose: {ten_numbers}')
    
# 13 - generate 10 random numbers from -100-100 

ten_numbers = []

while True:
    random_num = random.randrange(-100,100)
    if len(ten_numbers) == 9:
        break
    else:
        ten_numbers.append(random_num)

print(ten_numbers)
        
# 14

numbers = []
number_list_length = random.randrange(50,100)

while True:
    random_num = random.randrange(0,1000)
    if len(numbers) == number_list_length:
        break
    else:
        numbers.append(random_num)

print(len(numbers))


# Exercise 3: Working On A Paragraph

paragraph = (
"En los últimos años, la longevidad cerebral ha cobrado protagonismo "
"en las preocupaciones de salud, tanto en investigaciones como en la vida cotidiana."
"Un nuevo estudio confirma que tocar un instrumento puede marcar la diferencia en la "
"preservación de las habilidades cognitivas, incluso en personas mayores."
)

# 20

characters = len(paragraph)

# split paragraph in sentences
sentences = paragraph.split('.')

# Remove /n characters for mid sentence
for index, sentence in enumerate(sentences):
    for char in sentence:
        if char == '\n':
            sentences[index] = sentence.replace('\n',' ')

sentences = [sentence.lstrip() for sentence in sentences]

# count words 
word_count = paragraph.count(' ') + 1

# check unique words 
words = paragraph.split(' ')

#Remove commas and dots from words
for index, word in enumerate(words):
    for char in word:
        if char == ',':
            words[index] = word.replace(',','')
        elif char == '.':
            words[index] = word.replace('.','')

# unique words
words_no_duplicates = set(words)

# count no whitespaces characters
commas_count = paragraph.count(',')
dots_count = paragraph.count('.')
whitespace_count = word_count - 1 
paragraph_length = len(paragraph)
non_whitespaces_count = paragraph_length - (commas_count + dots_count + whitespace_count)

# Average amount of words per sentence 

num_char_sentences = []
for sentence in sentences:
    sentence_char_count = len(sentence)
    num_char_sentences.append(sentence_char_count)

average_num_characters = round(sum(num_char_sentences)/len(num_char_sentences))

# Non-unique words in paragraph
non_unique_words = 0
words_counted = []

words = [word.lower() for word in words]

for word in words:
    if word in words_counted:
        continue
    else:
        count = words.count(word)
        if count > 1:
            non_unique_words += count
            words_counted.append(word) 

print(f"Your paragraph has:\n-Characters: {characters}\n-Sentences: {len(sentences)}\n-Words: {len(words)}\n-Unique words: {len(words_no_duplicates)}\n-Non-Whitespace characters: {non_whitespaces_count}\n-Average amount of words per sentence: {average_num_characters}\n-Non-Unique Words: {non_unique_words}"
)


# Exercise 4: Frequency Of The Words

user_input = input("Enter a sentence of your choice: ")
words_input = user_input.split(' ')
list_words_counted = []

for word in words_input:
    if word in list_words_counted:
        continue
    else:
        count = words_input.count(word)
        print(f"{word}: {count}")
        list_words_counted.append(word)
        