# # SORTING IN PYTHON .sort() or sorted()
# # Lists[], Tuples(), Dictionaries{"":""}, Objects

# # ----------- LISTS -----------
# we use sort for lists because they are MUTABLE

# fruits = ['banana', 'orange', 'apple', 'coconut']

# fruits.sort() # sorts A-Z or 1,2,3...
# fruits.sort(reverse=True) # sorts descending order 
# print(fruits)

# # ----------- TUPLES -----------
# # we use sorted for tuples because they are IMMUTABLE so we need a COPY of the tuple

# fruits = ('banana', 'orange', 'apple', 'coconut')
# fruits = sorted(fruits) # the sorted converts the tuple into a list 
# print(fruits)

# # sorting tuple and keep it as a tuple (don't convert to list
# fruits = tuple(sorted(fruits)) 
# print(fruits)

# # reverse - sort in descending order
# fruits = tuple(sorted(fruits, reverse=True)) 
# print(fruits)


# ----------- DICTIONARIES -----------

fruits = {'banana': 105,
          'orange': 73,
          'apple': 72,
          'coconut': 354
          }

# sorted = if used without .items() it returns a list of the keys 
# .items() = returns a tuple with keys and values (apple,72),(banana,105)...
# dict = converts the list of tuples into a dictionary 

fruits = dict(sorted(fruits.items()))
print(fruits)