# *ARGS AND KWARGS
# ARGS = ARGUMENTS - placeholder for LISTS, TUPLES, SETS
#      - *args - simple sequence
#      - used for passing MORE than one argument
 
# KWARGS = KEY WORD ARGUMENTS - placeholder for DICTIONARY
#      - **kwargs - complex sequence 



students = ['Harry', 'Ron', 'Hermione']

def welcome(*args):
    if args:
        for name in args:
            print(f'{name}, welcome!')
    else:
        print('You passed an empty list')

welcome('Camila', 'Niv', 'Tomas', 'David') 


def user_info(**kwargs):
    print(kwargs)
    for value in kwargs.values():
        print(value)

user_info(name = 'Juliana', email = 'ju@gmail.com', age = 30, is_online = True, pets = ['Cat', 'Turtle'])


