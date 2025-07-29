# Exercise 1: What's Your Name?

def get_full_name(first_name, last_name, middle_name=''):
    if middle_name == '':
        return f'{first_name.capitalize()} {last_name.capitalize()}'
    else:
        return f'{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}'

print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))


# Exercise 2: From English To Morse

