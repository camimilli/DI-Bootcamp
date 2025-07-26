# DICTIONARIES - No index, instead, we access using pairs (key-value, also known as "entry")
#                Ordered, changeable (mutable). No duplicates
#                KEY should be IMMUTABLE value (e.g: strings), can't be empty (can have data type "None")
#                VALUE can be ANY data type (int, string, list...)


# Creating a dictionary

dic_constructor = {'name': 'juliana',
                   'age': 35,
                   'pets': ['Mushu', 'Luna', 'Bamba']
                   }



student_info = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': 14,
    'address': 'Privet Drive, 4',
    'pets': ['Hedwig', 'Phoenix', 'Buckbeak'],
    'houses': {'main': 'Gryffindor', 'second':'Slytherin'},
    'best_friends': ('Ron Weasley', 'Hermione Granger')
}

# Accessing Data
print(student_info['last_name']) # Potter
print(student_info['houses']) # {'main': Gryffindor, 'secondary': 'Slytherin'}

print(student_info['pets'][1]) # Buckbeak

sample_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {"physics": 70,
                      "history": 80
                      }
        }
    }
}

# access a dictionary in a dictionary in a dictionary...
print(sample_dict["class"]['student']['marks']['history'])

# USING METHODS ON VALUES 
print(student_info['last_name'])
print(student_info['pets'][1]) # accessing value by index in list pets

# Add value to key in dictionary
student_info['pets'].append('Fenix') # using append to add item as pets is a list 
print(student_info['pets'])

# convert value to uppercase (first name is string)
student_info['first_name'].upper()
print(student_info)

# CHANGING VALUES
student_info['address'] = 'Hogwarts'
print(student_info['address'])

# DELETING A KEY 
del student_info['age']
print(student_info)

# CREATE NEW KEY-VALUE PAIR (adds to the end)
student_info['teachers'] = {'Dumbledore', 'Snape', 'McGonagall'}
print(student_info)

# EXERCISE 1 - access the value in key history

sample_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {"physics": 70,
                      "history": 80
                      }
        }
    }
}


print(sample_dict["class"]['student']['marks']['history'])


# LOOPS AND BUILT-IN METHODS FOR DICTIONARIES

# keys() - access keys 
for k in student_info.keys():
    print(k)

# values() - access values 
for v in student_info.values():
    print(v)

# items() - access key and value 
for key, value in student_info.items():
    print(key, value)

# using items() returns a dictionary object
#resembles a 2d list of tuples {(),(),()}
# first index is key, second index is value
#can also use one value for both k_value 
for key,value in student_info.items():
    print(f"{key}: {value}")

# update() - like append() for lists
# insert a NEW key-value pair or UPDATE an existing key-value pair
# better to use update than assignment form as it's more clear in code
student_info.update({'patronus': 'stag'})

# get() - returns the value of the specified key, if key doesn't exit return none 
print(student_info.get('pets')) # returns pets
print(student_info.get('Japan')) # returns None

# zip() - used to combine related information 
names = ['Camila', 'Niv', 'Mushu']
addresses = ['Ramat Gan', 'Jerusalem', 'Tel Aviv']

print(list(zip(names, addresses)))

# pop() like del but it returns the value you removed (del doesn't)
# takes an optional 2nd arg, default value to return if the key is not found (used to avoid KeyError)
student_info.pop('address')
print(student_info)

# popitem() - removes latest key-value pair inserted
student_info.popitem('pets')
print(student_info)

# clear() - deletes all key-value pairs in dictionary
student_info.clear()
print(student_info)

# EXERCISE 2 - Delete set of keys from Python Dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

keys_to_remove = ["name", "salary"]

for k in keys_to_remove:
    if k in sample_dict:
        del sample_dict[k]

print(sample_dict)


# creating dictionary where topic is key and grades is value
topics = ['Math', 'Grammar', 'History', 'Sports']
grades = [85, 90, 100, 75]

print(dict(zip(topics, grades)))

# if there are more topics than grades or vs it will ignore the 
# values that are left
topics = ['Math', 'Grammar', 'History', 'Sports']
grades = [85, 90, 100, 75, 87, 55, 25]

print(dict(zip(topics, grades)))