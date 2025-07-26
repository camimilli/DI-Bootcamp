# TUPLES 
# can't be changed, used for list of cities in Israel, countries in the world, tz numbers, passport numbers, language options...


# CREATING TUPLES
my_tuple2 = (13, 23)
empty_tuple = () # empty tuple
nums = [1,2,34,5,67]
nums_tuple = tuple(nums) # tuple builder is used to convert a list into a tuple


# TUPLE METHODS
# can't append/change elements to/in tupples as they are immutable but there are workarounds

# count how many times an element appears in tuple
city_codes = ('NY', 'BO', 'SP', 'IL', 'NY')
print(city_codes.count('NY'))

# Indexing 
print(city_codes[1]) # returns value on index 1 
city_codes.index('SP') # returns in which index value SP is located 

# Unpacking Tuple to variables
languages = ('EN', 'RU', 'ES', 'PT')

# first value in tuple will be assign to lang1, second to lang2 and so on...
lang1, lang2, lang3, lang4 = languages 
print(lang1) # EN
print(lang2) # RU
print(lang3) # ES
print(lang4) # PT



# SETS
# MAIN USE -> Don't allow duplicated values 
# Mutable (can change)
# Not considered sequence since not indexed, it's an unordered list
# Common usage case - extracting data from API that you don't want to have duplicates, you extract it as SET to avoid duplicate values and then store in database as LIST

# CREATE A SET 
some_set = set() # builder, you can create set straight or pass list
other_set = {1,2,6}

# accesing a set - can't, just can see if value in set 
my_set = {1,2,3,4,5}
print(1 in my_set) # to know if the value is in the set 


# METHODS
countries = {"Israel", "US", "Brazil"}
names = {"Shimon", "Israel", "David"}

# add() - adding one element to a set 
names2 = {"Camila", "Niv", "Gisela"}
names2.add("Ariel")
print(names2)

# update () append multiple elements to a set 
# takes an iterable (list, tuple, another set) as an argument and adds all unique elements
# from the provided iterable to the existing set 
my_fav_numbers = {1,3,9,5}
numbers_to_add = {15,25}
my_fav_numbers.update(numbers_to_add)


# difference() 
# Returns a set containing the difference between two or more sets

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set)) 

# difference_update()
# Removes all elements of another set from the first set you define

my_set.difference_update(your_set)
print(my_set)

# discard()
# Removes the specified item
print(my_set.discard(5))

# intersection()
# Returns a new set with elements common to the set and all others
print(my_set.intersection(your_set)) 
print(my_set & your_set) # same as doing intersection()

# isdisjoint()
# Returns True if two sets has a null intersection, do these sets have nothing in common?
print(my_set.isdisjoint())

# issubset()
# Tells you whether another set contains this set 
my_numbers = {4,5}
your_numbers = {4,5,6,7,8,9,10}
print(my_numbers.issubset(your_numbers))

# issuperset()
# Tells you whether this set contains the other set 
# The other way around of issubset()
print(my_numbers.issuperset(your_numbers))

# union()
# Returns a new set with elements from the set and all others
# good to make sure when you join two sets/lists you don't have duplicates
print(my_set.union(your_set))
print(my_set | your_set) - # same as using union 

# Exercise - check who didn't come to class 
school = {'Bobby','Tammy','Jammy','Sally','Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

non_attendance = school.difference(set(attendance_list))
print(non_attendance)



