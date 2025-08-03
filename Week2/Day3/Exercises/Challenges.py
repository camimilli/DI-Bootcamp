import math 

# # Exercise 1

# fruits = ['banana', 'mango', 'strawberry']

# def insert_item(my_list, my_index, my_value)->list:
#     my_list[my_index] = my_value
#     return my_list

# insert_item(fruits, 2, 'kiwi')
# print(fruits)


# # Exercise 2 

# long_string = 'this is a very long string \
# that allows me to write things \
# in this way'

# def whitespace_counter(text):
#     counter = 0 
#     for char in text:
#         if char == ' ':
#             counter += 1 
#     return counter 

# print(whitespace_counter(long_string))


# # Exercise 3

# def count_upper_lower(text):
#     upper_case = 0
#     lower_case = 0 
#     for char in text:
#         if char.isupper() == True:
#             upper_case += 1 
#         elif char.islower() == True:
#             lower_case += 1
#     return upper_case, lower_case

# upper_case, lower_case = count_upper_lower('This Is Something Incredible! WOW')
# print(f'Upper Case: {upper_case}\nLower case: {lower_case}')


# # Exercise 4 

# def my_sum(numbers)->int:
#   '''
#   Returns the sum of numbers
#   from a list of numbers
#   '''
#     total_sum = 0
#     for num in numbers:
#         total_sum += num
#     return total_sum


# Exercise 5 

# def find_max(numbers)->int:
#     '''
#     Returns the max number from a list of numbers
#     '''
#     largest_number = numbers[0]
#     for num in numbers: 
#         if  num > largest_number:
#             largest_number = num 
#     return largest_number 

# print(find_max([1,4,100,20,30,1000,1001,400]))


# Exercise 6

# def factorial(num):
#     factorial = 1
#     for number in range(1,num+1):
#         factorial *= number 
#     return factorial 

# print(factorial(4))


# Exercise 7 

# def list_count(my_list,value):
#     counter = 0
#     for element in my_list:
#         if element == value:
#             counter += 1 
#     return counter

# print(list_count(['c','a','a','o'],'c'))


# Exercise 8 

# def norm(numbers):
#     sum_squares = 0
#     for num in numbers:
#         sum_squares += (num ** 2)
#     return round(math.sqrt(sum_squares))

# print(norm([1,2,2]))


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
# def is_mono(array):
#     previous_number = array[0]
#     ascending = False
#     descending = False
#     list_length = len(array)-1

#     # descending
#     for i, num in enumerate(array):
#         if i == 0:
#             continue
#         elif i == list_length and num <= array[i-1]:
#             descending = True
#         elif num <= array[i-1]:
#             continue 
#         else:
#             break
    
#     # ascending
#     for i, num in enumerate(array):
#         if i == 0:
#             continue
#         elif i == list_length and num >= array[i-1]:
#             ascending = True
#         elif num >= array[i-1]:
#             continue 
#         else:
#             break
   

#     if descending == True or ascending == True:
#         return True
#     else:
#         return False 
    
# print(is_mono([7,6,5,5,2,0]))
# print(is_mono([2,3,3,3]))
# print(is_mono([1,2,0,4]))

# MORE EFFECTIVE WITH CHATGPT HELP

def is_mono(array):
    ascending = True
    descending = True 

    for i in range(1,len(array)):
        if array[i] < array[i - 1]:
            ascending = False
        elif array[i] > array[i - 1]:
            descending = False

    return ascending or descending 
    
print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))


















