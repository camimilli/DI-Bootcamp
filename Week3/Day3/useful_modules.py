# # RANDOM BUILT-IN MODULE

# import random 

# # help(random) # module documentation
# print(dir(random)) # methods available on this package if you add a . after random you can see all the available methods/attributes on a dropdown list

# random.random() # gives a random number between 0-1 
# random.randint() # gives a random number, 1st arg: start points / 2nd arg: end point 
# random.choice([1,2,3,4,5]) # give a choice to make - in this case it picks one element from the list randomly, useful for a game where you need a random generator or for pieces of tetris you want to pick
# random.shuffle() # can use it to shuffle a list 


# Sys BUILT-IN MODULE
# sys module provides access to system-specific parameters and functions. 
# Allows you to interact with the Python interpreter itself. Can use it to access command-line arguments, manage the search path for modules and exit the program.



# Datetime and Array BUILT-IN MODULES

# DATETIME 

import datetime 

print(datetime.time(5,45,2)) # 05:45:02 
print(datetime.date.today()) # returns today's date

# ARRAY
# Arrays take up less memory than lists and perform faster
# If you have large lists you can improve them with an array 
# SYNTAX - array(typecode, values)   typecode = type of data this array will use 
from array import array 

arr = array('i', [1,2,3])
print(arr[0]) # can access elements like with lists