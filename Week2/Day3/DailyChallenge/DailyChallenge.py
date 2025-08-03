# Daily Challenge: Advanced Algorithm

# import random

# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

# target_number   = 3728

# numbers_checked = []

# def pairs_sum(numbers):
#     for num1 in numbers:
#         for num2 in numbers:
#             if num1 not in numbers_checked or num2 not in numbers_checked:
#                 if num1 + num2 == target_number:
#                     numbers_checked.append(num1)
#                     numbers_checked.append(num2)
#                     print(f'{num1} and {num2} sums to the target number {target_number}')
                    
    
# print(pairs_sum(list_of_numbers))

list_of_numbers = [1000, 2728, 1864, 1864, 500, 3000, 100, 3628, 2000, 1728]
target_number = 3728

# More efficient solution

def pairs_sum(numbers):
    seen = set() # Notebook of numbers we've seen
    pairs = set() # Store unique pairs 

    for num in numbers:
        complement = target_number - num 

        if complement in seen:
            # Store pair in a sorted tuple to avoid (a,b) and (b,a) duplicates
            pairs.add(tuple(sorted((num, complement))))

        seen.add(num)

    for num1, num2 in pairs:
        print(f'{num1} and {num2} sums to the target number {target_number}')


pairs_sum(list_of_numbers)

