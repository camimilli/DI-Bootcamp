# RANDOM BUILT-IN MODULE

import random 

# help(random) # module documentation
print(dir(random)) # methods available on this package if you add a . after random you can see all the available methods/attributes on a dropdown list

random.random() # gives a random number between 0-1 
random.randint() # gives a random number, 1st arg: start points / 2nd arg: end point 
random.choice([1,2,3,4,5]) # give a choice to make - in this case it picks one element from the list randomly, useful for a game where you need a random generator or for pieces of tetris you want to pick
random.shuffle() # can use it to shuffle a list 


# Sys BUILT-IN MODULE
