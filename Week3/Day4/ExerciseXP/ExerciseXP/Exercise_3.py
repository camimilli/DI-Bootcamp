# Exercise 3: String Module

import string, random

# One solution 
letters = string.ascii_letters 
random_string = ''

for _ in range(5):
    random_string += random.choice(letters)

# Another solution
# result = ''.join(random.choice(letters) for _ in range(5))
# print(result)
