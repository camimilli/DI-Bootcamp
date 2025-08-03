import math 

# Exercise 1

fruits = ['banana', 'mango', 'strawberry']

def insert_item(my_list, my_index, my_value)->list:
    my_list[my_index] = my_value
    return my_list

insert_item(fruits, 2, 'kiwi')
print(fruits)

########################################

# Exercise 2 

long_string = 'this is a very long string \
that allows me to write things \
in this way'

def whitespace_counter(text):
    counter = 0 
    for char in text:
        if char == ' ':
            counter += 1 
    return counter 

print(whitespace_counter(long_string))

########################################

# # Exercise 3

def count_upper_lower(text):
    upper_case = 0
    lower_case = 0 
    for char in text:
        if char.isupper() == True:
            upper_case += 1 
        elif char.islower() == True:
            lower_case += 1
    return upper_case, lower_case

upper_case, lower_case = count_upper_lower('This Is Something Incredible! WOW')
print(f'Upper Case: {upper_case}\nLower case: {lower_case}')

########################################

# # Exercise 4 

def my_sum(numbers)->int:
  '''
  Returns the sum of numbers
  from a list of numbers
  '''
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

########################################

# Exercise 5 

def find_max(numbers)->int:
    '''
    Returns the max number from a list of numbers
    '''
    largest_number = numbers[0]
    for num in numbers: 
        if  num > largest_number:
            largest_number = num 
    return largest_number 

print(find_max([1,4,100,20,30,1000,1001,400]))

########################################

# Exercise 6

def factorial(num):
    factorial = 1
    for number in range(1,num+1):
        factorial *= number 
    return factorial 

print(factorial(4))

########################################

# Exercise 7 

def list_count(my_list,value):
    counter = 0
    for element in my_list:
        if element == value:
            counter += 1 
    return counter

print(list_count(['c','a','a','o'],'c'))

########################################

# Exercise 8 

def norm(numbers):
    sum_squares = 0
    for num in numbers:
        sum_squares += (num ** 2)
    return round(math.sqrt(sum_squares))

print(norm([1,2,2]))

########################################

# Exercise 9 

# def is_mono(numbers)->bool:
#     previous_number = numbers[0]
#     ascending = False
#     descending = False 
#     checking_desc_asc = False
#     list_length = len(numbers)-1

#     while checking_desc_asc == False: 
# # while ascending == False:
#         # checking if array ascending 
#         for index, num in enumerate(numbers):
#             if index == list_length and num == numbers[list_length] and previous_number <= num:
#                 ascending = True 
#                 break
#             if previous_number <= num:
#                 previous_number = num 
#                 continue 
#             elif previous_number >= num:
#                 break
                

#         previous_number = numbers[0]

# # while descending == False:

#         # check if array descending
#         for index, num in enumerate(numbers):
#             if index == list_length and num == numbers[list_length] and previous_number >= num:
#                 descending = True 
#                 break
#             elif previous_number >= num:
#                 previous_number = num 
#                 continue 
#             else: 
#                 break
        
#         checking_desc_asc = True
    
#     if (ascending == True) or (descending == True):
#         return True 
#     else:
#         return False 
    
         
# print(is_mono([7,6,5,5,2,0]))
# print(is_mono([2,3,3,3]))
# print(is_mono([1,2,0,4]))

# MORE EFFECTIVE 
def is_mono(array):
    previous_number = array[0]
    ascending = False
    descending = False
    list_length = len(array)-1

    # descending
    for i, num in enumerate(array):
        if i == 0:
            continue
        elif i == list_length and num <= array[i-1]:
            descending = True
        elif num <= array[i-1]:
            continue 
        else:
            break
    
    # ascending
    for i, num in enumerate(array):
        if i == 0:
            continue
        elif i == list_length and num >= array[i-1]:
            ascending = True
        elif num >= array[i-1]:
            continue 
        else:
            break
   

    if descending == True or ascending == True:
        return True
    else:
        return False 
    
print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))

# MORE EFFECTIVE WITH CHATGPT HELP

# def is_mono(array)->bool:
    #   '''
    #   Returns True if the array passed to the function
    #   is sorted in ascending or descending order 
    #   else returns False 
    #   '''
#     ascending = True
#     descending = True 

#     for i in range(1,len(array)):
#         if array[i] < array[i - 1]:
#             ascending = False
#         elif array[i] > array[i - 1]:
#             descending = False

#     return ascending or descending 
    
# print(is_mono([7,6,5,5,2,0]))
# print(is_mono([2,3,3,3]))
# print(is_mono([1,2,0,4]))

########################################

# # Exercise 10

def longest_word(array)->str:
    '''
    prints the longest word in a list 
    '''
    print(max(array, key=len))

longest_word(['potato','mamushka','onomatopeya'])

########################################

# # Exercise 11 

# My solution 
def integers_and_strings(array):
    strings = [element for element in array if type(element) == str]
    integers = [element for element in array if type(element) == int]
    return strings, integers

# Solution with CHATGPT (does the appending in one loop, not in two)

# def integers_and_strings(array):
#     strings = []
#     integers = []

#     for element in array:
#         if isinstance(element, str):
#             strings.append(element)
#         elif isinstance(element, int):
#             integers.append(element)

#     return strings, integers


# strings, integers = integers_and_strings(['hello', 2, 3, 'miau', 4, 5, 3, 'bye'])
# print(strings)
# print(integers)

########################################

# Exercise 12 

def is_palindrome(word)->bool:
    word_backwards = ''
    for i in range(len(word)-1, -1, -1):
        word_backwards += word[i]
    
    if word.lower() == word_backwards.lower():
        return True
    else:
        return False 
    
print(is_palindrome('radar'))
print(is_palindrome('John'))

word = 'camila' 
print(word[::-1].lower())


# chat gpt more efficient solution 

# def is_palindrome(word):
#     return word == word[::-1].lower()

########################################

# Exercise 13 

def sum_over_k(sentence, k)->int:

    list_words = sentence.split(' ')
    longer_k = [word for word in list if len(word) > k]
    return len(longer_k)


sentence = 'Do or do not there is no try'
print(sum_over_k(sentence, 2))

########################################

# # Exercise 14

def dict_avg(my_dic)->int:
    '''
    Returns the average value in a dictionary
    '''
    total_sum = sum(my_dic.values())
    length_dic = len(my_dic.values())

    return round(total_sum / length_dic)

print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))

########################################

# Exercise 15 

def common_div(first_num, second_num)->list:
    first_num_divisors = set([num for num in range(1,first_num+1) if (first_num % num == 0)])
    second_num_divisors = set([num for num in range(1,second_num+1) if (second_num % num == 0)])
    common_div = list(first_num_divisors.intersection(second_num_divisors))
    common_div.sort()
    return common_div

print(common_div(10,20))


# chat gpt more efficient solution

# def common_div(first_number, second_number)->list:
#     limit = min(first_number, second_number)
#     common_divisors = [num for num in range(1, limit + 1) if first_number % num == 0 and second_number % num == 0]
#     return common_divisors

# print(common_div(10,20))

########################################

# Exercise 16

def is_prime(number)->bool:

   for num in range(2, number):
        if number % num == 0:
            return False
    
   return True

########################################

# Exercise 17

def weird_print(array)->list:
    '''
    Prints elements of a list if the index \
    and the value are even 
    '''

    even_values = [value for index, value in enumerate(array) if index % 2 == 0 and value % 2 == 0]
    return even_values

print(weird_print([1,2,2,3,4,5]))

########################################

# Exercise 18

def type_count(**kwargs)-> int:
    '''
    Accepts an undefined number of keyworded arguments \
    and returns the count of different types (int, str, float, bool)
    '''
    for value in kwargs.values():
        if (isinstance(value, bool)): 
            bool_count += 1
        elif (isinstance(value, str)):
            str_count += 1
        elif (isinstance(value, float)):
            float_count += 1
        elif (isinstance(value, int)):
            int_count += 1
    
    return int_count, str_count, float_count, bool_count


int_count, str_count, float_count, bool_count = type_count(a=1,b='string',c=1.0,d=True,e=False)
print(f'int: {int_count}, str: {str_count}, float: {float_count}, bool: {bool_count}')

########################################

# Exercise 19

def split_text(text, character)->list:
    '''
    Splits a string into a list based on \
    the character passed 
    '''

    new_list = []

    temp_string = ''

    for char in text:
        if char != character:
            temp_string += char 
        elif char == character:
            new_list.append(temp_string)
            temp_string = ''

    if temp_string != '':
        new_list.append(temp_string)

    return new_list

print(split_text('banana@apple@mango@hey@@','@'))

########################################

# Exercise 20 

def password_format(text)->str:
    '''
    Converts a string into password format
    '''
    output = '*' * len(text)
    return output 

input = 'mypassword'
output = password_format(input)
print(f'input: {input}\noutput: {output}')