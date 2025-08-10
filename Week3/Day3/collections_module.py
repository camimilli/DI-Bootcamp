# Collections = Provide additional data structures for collections of data 

##########################################

# Defaultdict
# same as dict, difference is that it doesn't give an exception/key error when you try to access the non-existent key
# SYNTAX = my_dict = defaultdict(type)
# Type defines default value returned 
#       - int() returns 0 
#       - list() returns []
#       - set() returns set()

from collections import defaultdict, Counter, deque, namedtuple, ChainMap, OrderedDict

# Example 1 
nums = defaultdict(int) # we use int as it tells the defaultdict what value to use by default 

nums['one'] = 1 
nums['two'] = 2 
nums['three'] = 3 
print(nums['four']) # prints 0 even if 'four' key doesn't exist
print(nums) # now you'll see that 'four' was added to the list with value 0 

# Example 2 - counting elements

mylist = [1,2,3,2,1,3,4,5,1,2]

# if I'd initialize an empty dict the for loop wouldn't work as the keys were not initiated
counter = defaultdict(int)

# good as we don't need to initialize it as 0 
# because the key will be added automatically even if it doesn't exist
for element in mylist:
    counter[str(element)] += 1 

print(counter)


# Example 3 - grouping elements

words = ['apple', 'banana', 'carrot', 'avocado', 'brocoli', 'orange']

grouped_words = defaultdict(list)

for word in words:
    grouped_words[word[0]].append(word)

print(grouped_words)


# Example 4 - grouping and adding 

# want to combine the same key and add their values into a list 
tuple_list =  [("A", 10), ("B", 4), ("A", 5), ("C", 7), ("B", 1)]

grouped_data = defaultdict(list)

for key, value in tuple_list:
    grouped_data[key].append(value)

print(grouped_data)

# sum the values 
grouped_data = {k: sum(v) for k, v in grouped_data.items()}
print(grouped_data)

##########################################

# Counter
# SYNTAX - variable = Counter(data)
c = Counter('gallad') # counts every string 
print(c) # Counter({'a': 2, 'l': 2, 'g': 1, 'd': 1})

c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c) # Counter({'a': 2, 'c': 2, 'b': 1})

c = Counter({'a': 1, 'b': 2})
print(c) # Counter({'b': 2, 'a': 1})

c = Counter(cats=4, dogs=7) 
print(c) # Counter({'dogs': 7, 'cats': 4})
print(c['cats']) # 4 

print('##############\n')

# Example 2 
list = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 1, 2, 2]
answer = Counter() # converts it into a counter object 
print(answer)
answer = Counter(list) # puts a list and counts how many time each element appears in the list 
print(answer[2]) # print how many times 2 appears, as 2 is the key in the dict 

print('##############\n')

##########################################

# deque - good for when you work with queues 
# adds + functionalities to lists

people = ['Mario', 'Luigi', 'Toad']
queue = deque(people) # converts list into a deque data type 

queue.append('Bowser')
print(queue)

# In normal list we can pop elements from the end of the list
# with popleft we can remove from the beginning of the list
queue.popleft()
print(queue)

# adds the element at the beginning of the list 
# on lists you can only append to the end of the list
queue.appendleft('Daisy')
print(queue)

# Rotation
# -1 moves everyone to the left 1 place 
# no value passed moves everyone 1 place to the right 
# you can also add any number you want -2, etc...
queue.rotate(-1)
print(queue)

queue.rotate()
print(queue)

# Append more than one element to the END of the list 
queue.extend(['Shy Guy', 'Yoshi'])
print(queue)

# Append more than one element to the BEGINNING of the list 
queue.extendleft(['Shy Guy', 'Yoshi'])
print(queue)

# Reverse 
queue.reverse()
print(queue)

print('##############\n')

##########################################

# Namedtuple()

# regular tuple 
color = (55,155,255)

# accessing value 55 from color, no context for other dev what color[0] is 
print(color[0])
# we could use a dictionary color = {'red': 55, 'green': 155, 'blue': 255}
# but sometimes there's a reason why we need tuples (immutable) and dictionaries need more typing

# using namedtuple() 
# SYNTAX = namedtuple(name_of_tuple, [values of the tuple])
Color = namedtuple('Color', ['red', 'green', 'blue'])

# creating a tuple using the Color we created 
color = Color(55,155,255)
color = Color(red=55, green=155, blue=255) # you can also do this to assign values to tuple

print(color[0]) # can still access tuple by index 
print(color.red) # adds functionality of accessing tuple by name 

# creating a new color with its red, green and blue values
white = Color(255, 255, 255)
print(white.blue) # print the blue value of white color (255)

print('##############\n')

##########################################

# ChainMap
# combines a lot of dictionaries together and returns a list of dictionaries

dictionary1 = {'a' : 1, 'b' : 2}
dictionary2 = {'c' : 3, 'b' : 4}
chain_Map = ChainMap(dictionary1, dictionary2)
print(chain_Map.maps) # [{'a': 1, 'b': 2}, {'c': 3, 'b': 4}]

print('##############\n')

##########################################

# OrderedDict 
# https://www.youtube.com/watch?v=kQ9O4T9WewM
# python 3.7 > makes dictionaries ordered, OrderedDict still gives more functionality that can help
# SYNTAX - od: OrderedDict[data type key, data type value] = OrderedDict({key: value, key: value...})

od: OrderedDict[str, int] = OrderedDict({'a': 1, 'b': 2, 'c': 3})
print(od) # OrderedDict({'a': 1, 'b': 2})

# popitem() with additional value
od.popitem(last=False) # we pop the first item in the dict instead of the last as pop would do
popped = od.popitem(last=False) # we can pop and assign that pop value into a variable

od: OrderedDict[str, int] = OrderedDict({'a': 1, 'b': 2, 'c': 3})

# move_to_end - moves a specific item to the end of the dictionary
# od.move_to_end('a') # moves key 'a' from the beginning to the end of the dictionary
od.move_to_end('c', last=False) # it will move c which is at the end to the beginning of the list because we used last=False 
# false makes the beginning the end 
print(od)


