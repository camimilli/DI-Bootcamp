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

# METHODS
countries = {"Israel", "US", "Brazil"}
names = {"Shimon", "Israel", "David"}

# adding one element to a set 
names2 = {"Camila", "Niv", "Gisela"}
names2.add("Ariel")
print(names2)

# update () append multiple elements to a set 
# takes an iterable (list, tuple, another set) as an argument and adds all unique elements
# from the provided iterable to the existing set 
my_fav_numbers = {1,3,9,5}
numbers_to_add = {15,25}
my_fav_numbers.update(numbers_to_add)



# Intersection - Adds the SHARED values of two sets in a new set 
set_3 = countries.intersection(names)
print(set_3)

# Union - Merging UNIQUE values of two different sets in a new set 
# Good way to make sure that when you merge two sets you are not repeating values
merged_set = countries.union(names)
print(merged_set)

