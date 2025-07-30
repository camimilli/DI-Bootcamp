# *ARGS AND KWARGS
# ARGS = ARGUMENTS - placeholder for LISTS, TUPLES, SETS
#      - *args - simple sequence
#      - used for passing MORE than one argument
 
# KWARGS = KEY WORD ARGUMENTS - placeholder for DICTIONARY
#      - **kwargs - complex sequence
 
# RULE for PARAMETERS in function:
# params, *args, default parameters, **kwargs

########################################

# USING *ARGS
students = ['Harry', 'Ron', 'Hermione']

def welcome(*args):
    if args:
        for name in args:
            print(f'{name}, welcome!')
    else:
        print('You passed an empty list')

welcome('Camila', 'Niv', 'Tomas', 'David') 

########################################

# USING **KWARGS
def user_info(**kwargs):
    print(kwargs)
    for value in kwargs.values():
        print(value)

user_info(name = 'Juliana', email = 'ju@gmail.com', age = 30, is_online = True, pets = ['Cat', 'Turtle'])

########################################
# USING *ARGS AND **KWARGS TOGETHER

def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

########################################


