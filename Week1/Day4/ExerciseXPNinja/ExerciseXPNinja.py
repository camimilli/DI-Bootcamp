# # Exercise 1: Formula
import math

# C = 50 
# H = 30

# # Ask user for numbers
# user_input = input("Enter a comma-separated string of numbers: ")
# numbers_string = user_input.split(",")

# # Convert numbers to integers 
# numbers = [int(num) for num in numbers_string]

# # Apply square root to numbers 
# for index, num in enumerate(numbers):
#     numbers[index] = round(math.sqrt((2 * C * num)/H))
   
# # print numbers
# print(*numbers_string, sep=', ')


# Exercise 2: List Of Integers

numbers_1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
numbers_2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
numbers_3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
numbers_4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# 1
all_numbers = numbers_1 + numbers_2 + numbers_3 + numbers_4

# # 2a 
# print(all_numbers)

# # 2b
# all_numbers_sorted_reverse = sorted(all_numbers, reverse=True)
# print(all_numbers_sorted_reverse)

# # 2c 
# print(sum(all_numbers))

# # 3
# first_and_last = [all_numbers[0], all_numbers[-1]]
# print(first_and_last)

# # 4 
# greater_than_50 = list((num for num in all_numbers if num > 50))
# print(greater_than_50)

# # 5
# smaller_than_10 = list(num for num in all_numbers if num < 10)
# print(smaller_than_10)

# # 6 
# squared_numbers = list(round(math.sqrt(num)) for num in all_numbers if num > 0)
# print(squared_numbers)

# # 7
# all_numbers_no_duplicates = set(all_numbers)
# all_numbers_no_duplicates = list(all_numbers_no_duplicates)
# print(all_numbers_no_duplicates)

# # 8
# average = round(sum(all_numbers) / len(all_numbers))
# print(average)

# # 9
# print(max(all_numbers))

# # 10
# print(min(all_numbers))

# # 11
# # sum 
# sum_numbers = 0

# for num in all_numbers:
#     sum_numbers += num

# print(sum_numbers)

# # average 
# average_result = round(sum_numbers / len(all_numbers))
# print(average_result)

# # largest number

# largest_num = all_numbers[0]

# for num in all_numbers:
#     if num > largest_num:
#         largest_num = num
        
# print(largest_num)

# # smallest number

# smallest_number = all_numbers[0]

# for num in all_numbers:
#     if num < smallest_number:
#         smallest_number = num
        
# print(smallest_number)

