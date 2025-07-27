# Exercise 1: Birthday Look-Up

birthday = {'Camila': '1995/03/27',
            'Niv': '1994/10/08',
            'Gisela': '1984/09/22',
            'Natalia': '1995/05/09',
            'Kristen': '1998/02/07'
            }

print(f'Welcome to the birthday machine! 🥳\nYou can look up the birthdays of the people in the list!:\n{list(birthday.keys())}\nType "q" to quit')

while True:
    name_input = input('Enter a name:\n')
    if name_input == 'q':
        break
    elif name_input in birthday:
        print(f'{name_input}\'s birthday: {birthday[name_input]}')
    else:
        print('The name you wrote is not in our list :( try again)')