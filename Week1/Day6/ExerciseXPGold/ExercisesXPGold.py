# Exercise 1, 2, 3: Birthday Look-Up, Birthdays Advanced, Add Your Own Birthday

birthday = {'Camila': '1995/03/27',
            'Niv': '1994/10/08',
            'Gisela': '1984/09/22',
            'Natalia': '1995/05/09',
            'Kristen': '1998/02/07'
            }

print("Welcome to the birthday machine! 🥳")

while True:
    name_birthday = input("Enter the name of the person you want to add to the dictionary:\n")
    birthday_date = input("Enter their birthday date in YYYY/MM/DD format:\n")
    birthday.update({name_birthday:birthday_date}) 
    print(f"You can look up the birthdays of the people in the list!:\n{list(birthday.keys())}\nType 'q' to quit'")
    birthday_name_check_input = input('Enter a name:\n')
    if birthday_name_check_input == 'q':
        break
    elif birthday_name_check_input in birthday:
        print(f'{birthday_name_check_input}\'s birthday: {birthday[birthday_name_check_input]}')
    else:
        print('The name you wrote is not in our list :( try again)')


# Exercise 4: Fruit Shop

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

vowels = ('a', 'e', 'i', 'o', 'u')

for fruit,cost in items.items():
    if fruit[0] in vowels:
        print(f" An {fruit} costs: ${cost}")
    else:
        print(f" A {fruit} costs: ${cost}")

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_price = 0 

for fruit in items.keys():
    price = items[fruit]['price']
    stock = items[fruit]['stock']
    total_price += price * stock

# print(brand['major_color']['US'])

print(f"Total cost: ${round(total_price)}")