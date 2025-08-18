# LIST METHODS

# map(function, collection) - applies a given function to all items in a collection

# doing it with function
def c_to_f(temp):
    return (temp * 9/5) + 32

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

fahrenheit_temps = list(map(c_to_f, celsius_temps)) # map function returns a map object, we can convert to a list to display it

print(fahrenheit_temps)

# doing it with lambda instead of function 

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

fahrenheit_temps = list(map(lambda temp:(temp * 9/5) + 32, celsius_temps)) # map function returns a map object, we can convert to a list to display it
print(fahrenheit_temps)

#########################

# filter() returns an iterator where the items are filtered through a function to test if the item is accepted or not (function needs to return true or false)
my_list = [1,2,3]

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list))) # [1, 3] -> odd numbers

#########################

# zip() - iterates through the data structures given and zips them together in a tuple inside a list

list1 = ['camila', 'niv', 'gisela']
list2 = ['054-2537998', '052-4345944', '054-222-3454']

print(list(zip(list1, list2))) # [('camila', '054-2537998'), ('niv','052-4345944'), ('gisela','054-222-3454')]

list3 = [1, 2, 3]
list4 = (10, 20, 30)
list5 = (5, 4, 3)

print(list(zip(list3, list4, list5))) # [(1, 10, 5), (2, 20, 4), (3, 30, 3)]

#########################

# reduce(function, sequence, initial)

from functools import reduce 

camila_list = [1,2,3]

# item will be the first item in the list you pass in reduce
# acc default will be 0 if you don't define it 
def accumulator(acc, item):
    print(acc, item)
    return acc + item
     
print(reduce(accumulator, camila_list, 0))