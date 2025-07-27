# Exercise 1: Converting Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dictionary = dict(zip(keys,values))
print(new_dictionary)


# Exercise 2: Cinemax #2

family = {}
total_cost = 0

# Get input from user 
while True:
    name_input = input("Enter your name (type 'q' to quit):\n")
    if name_input == 'q':
        break
    else:
        age_input = input("Enter your age:\n")
        age_input = int(age_input)
        family.update({name_input: age_input})

# Calculate ticket per person and total 
for name, age in family.items():
     if age < 3:
         total_cost += 0 
         print(f"Ticket cost for {name}: $0")
     elif age in range(3,13):
         total_cost += 10
         print(f"Ticket cost for {name}: $10")
     else:
         total_cost += 15
         print(f"Ticket cost for {name}: $15")

print(f"Tickets Total Cost: ${total_cost}")


# Exercise 3: Zara

brand = {'name': 'Zara',
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona',
        'type_of_clothes': ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H&M', 'Benetton'],
        'number_stores': 7000,
        'major_color': {
            'France': 'blue',
            'Spain': 'red',
            'US': ['pink', 'green']
            }
        }

brand['number_stores'] = 2

print('In Zara you can buy items for: ')
for item in brand['type_of_clothes']:
    print(f'- {item}')


brand.update({'country_creation': 'Spain'})

if brand.get('international_competitors'):
    brand['international_competitors'].append('Desigual')

del brand['creation_date']

print(brand['international_competitors'][-1])

print(brand['major_color']['US'])

brand_list = list(brand)
print(len(brand_list))

for keys in brand.keys():
    print(keys)

# Bonus
more_on_zara = {
                'creation_date': 1975
}

brand.update(more_on_zara)
print(brand)


# Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
users_sorted = sorted(users)

characters_to_indexes = {}
indexes_to_characters = {}
characters_to_indexes_sorted = {}

# create a dictionary that maps characters to their indexes (original order)
for index,character in enumerate(users):
    characters_to_indexes.update({character:index})
    indexes_to_characters.update({index:character})

# create a dictionary that maps characters to their indexes (alphabetical order)
for index,character in enumerate(users_sorted):
    characters_to_indexes_sorted.update({character:index})

print(characters_to_indexes)
print(indexes_to_characters)
print(characters_to_indexes_sorted)

