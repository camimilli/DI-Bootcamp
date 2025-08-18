# List/Set Comprehension 
# Quick way to create lists/sets in python instead of appending/looping 
# my_list = [expression, variable and loop with iterable, condition (optional)]

my_list = [char for char in 'hello']
my_list2 = [num*2 for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)