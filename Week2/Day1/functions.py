# FUNCTIONS = A block of reusable block code 
#             place () after the function name to invoke it
#             include documentation ''' documentation ''' this shows when you hover on the function in the code

# SYNTAX

def func_name():
    '''prints a string on the console'''
    print("I am a function")

func_name() # calling the function

# EXERCISE 1 
# Create a function that prints "hello there!", then call the function to see the output

def hello_there():
    '''prints "hello there!' on the console'''
    print('hello there!')

hello_there()

print()

# Passing ARGUMENTS to the function
# the order of the arguments when calling the function matter 
# unless you use key word arguments

def greetings(language,name):
    '''prints a greeting depending on the language available'''
    if language == 'PT':
        print(f'Ola {name}, tudo bem?')

    elif  language == 'ES':
        print(f'Hola {name}, que tal?')

    else:
        print("Unknown language")

greetings('PT','Camila')


# Key word arguments

def greetings(language,name):
    '''prints a greeting depending on the language available'''
    if language == 'PT':
        print(f'Ola {name}, tudo bem?')

    elif  language == 'ES':
        print(f'Hola {name}, que tal?')

    else:
        print("Unknown language")

greetings(name = 'Camila', language = 'PT')


# Default value arguments
# if you want to give default value for 1 arg only, you need to move that arg to the end of the list of args

def greetings(language = 'EN', name= 'user')->str: #default values
    '''prints a greeting depending on the language available'''
    if language == 'PT':
        return f'Ola {name}, tudo bem?'

    elif  language == 'ES':
        return f'Hola {name}, que tal?'

    elif language == 'EN':
        return f'Hello {name}, how are you?'

    else:
        return "Unknown language"

greetings()

# Returning a value

def calculation(num1,num2):
    '''sums two inputed numbers'''
    result = num1 + num2
    return result 

print(calculation(5,3))

def multiply(calc)->int: # ->int adds on the doc that it returns an int
    '''takes a number and multiplies it by 5'''
    result = calc * 5
    return result

calc = calculation(5,3)
print(multiply(calc))

# EXERCISE 2
# create a function called country_info that receives a country name as an argument
# and prints the capital of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed

def country_info(country='Naboo')->str:
    '''Returns the capital of the input country'''
    if country == 'Naboo':
        capital = 'Theed'
        population = 1000
        return capital, population # python return a tuple, then we can unpack
    
    elif country == 'Argentina':
        capital = 'Buenos Aires'
        population = 43000000
        return capital, population
    
    elif country == 'Rusia':
        capital = 'Moscow'
        population = 143800000
        return capital, population
    
    elif country == 'Uruguay':
        capital = 'Montevideo'
        population = 23000000
        return capital, population 
    
    elif country == 'France':
        capital = 'Paris'
        population = 143800000
        return capital, population 
    
    else:
        return f'unknown'
    
print(country_info('Argentina')) # returns tuple

ar_capital, ar_pop = country_info('Argentina') # unpacking tuple into variables
print(ar_capital)
print(ar_pop)

# Global and Local Scopes
# Variables from global scopes can be accesed in any place of our file, like local scope but NOT modified 
# Variables from local scopes can't be accesed/modified on the global scope, only on local

age = 25 # variable in global scope 

def current_age():
    print(age) # we can access the global scope variable from the local scope, that's why it prints when we call the funtion
    my_age = 35 # variable in local scope, can't be accessed on global scope (if we try to do print(my_age) we'll get my_age is not defined)
    my_age += 1

current_age()

# this gives an error - you're trying to modify a global variable in the scope 
# def happy_birthday():
#     age += 1
#     print(age)

# happy_birthday()

# modifying global variable in local scope 
def happy_birthday():
    global age # python recognizes is a global variable and allows modifications
    age += 1 
    print(age)

happy_birthday()

