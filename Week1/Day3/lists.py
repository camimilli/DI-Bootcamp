user_name = 'camimilli'
email = 'cami.milli@gmail.com'
user_age = 30
is_online = True

user_info = [user_name, email, user_age, is_online]
print(len(user_info))

# CREATING LISTS

some_list = list('item 1') # list function creates list of lists -> ['i', 't', 'e', 'm', '', '1']
other_list = ['item 1'] # takes argument and puts it inside a list -> ['item 1']

print(some_list)
print(other_list)

empty_list = [] # creates an empty list


# INDEXING AND SLICING 

# Indexing - Ordered means it can be accessed by index
print(user_info[2]) 

# slicing 
fruits = ['orange', 'kiwi', 'apple', 'banana']
print(fruits[-2:]) # returns last two elements of the list

# Changing element to another element
# strings are immutable - can't change a character in a string, we can do it in lists
fruits[1] = 'pineapple' # changes 'kiwi' for 'pineapple'
print(fruits) 

# LIST METHODS

# Insert new item at specific index 
fruits = ['orange', 'kiwi', 'apple', 'banana']
fruits.insert(1, 'mango') # takes 2 args -> index and what to insert
print(fruits)

# Remove an element 
fruits.remove('kiwi') # if you have 2 kiwis in the list, it will remove first appearence
print(fruits)

# Add an item at the end of a list one at a time
# if you pass a list it will append the list as a list and not its elements
fruits.append('watermelon')
print(fruits)

# Remove last item of list or by index
fruits.pop() # removed last item of list
print(fruits)
fruits.pop(0) # removes item on index 0 

# Joins the elements of a list to another list - can only pass ONE argument
veggies = ['tomato', 'cucumber', 'potato', 'carrot']
fruits.extend(veggies)

# Clear list - removing all elements
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.clear()
print(basket)

# .sorted() and .sort() - Sorts by A-Z 
# Sort by Z-A -> list.sort(reverse=True)

# .sorted() creates a new list 
fruits_sorted = sorted(fruits)
print(fruits)
print(fruits_sorted)
fruits_sorted = sorted(fruits, reverse=True) # sorts Z-A
print(fruits_sorted)

# .sort() changes the original list 
fruits.sort() # sorts A-Z 
print(fruits)
fruits.sort(reverse=True) # sorts Z-A 
print(fruits)

# EXERCISE 1
list1 = [5, 10, 15, 20, 25, 50, 20]
index_20 = list1.index(20)

if 20 in list1: 
    list1[index_20] = 200

print(list1)


# LIST COMPREHENSION = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      Syntax - [expression for value in iterable if condition]

# List iteration with normal loop 
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)


# Same example with list comprehension
doubles = [x * 2 for x in range(1,11)]

# Good for creating new lists
fruits = ['apple', 'orange', 'banana', 'coconut']
uppercase_fruits = [fruit.upper() for fruit in fruits] # capitalize every fruit and add to new list
fruit_chars = [fruit[0] for fruit in fruits] # take first letter of every item in the list add to a new list

# List comprehension + conditions
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0] # when there's no expression (no value change) we just return the item (number) to add it to the list
print(positive_nums)
negative_nums = [num for num in numbers if num < 0]
print(negative_nums)
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [num for num in grades if num >= 60]
print(passing_grades)

