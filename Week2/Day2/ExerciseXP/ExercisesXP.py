import random 

# Exercise 1: What Are You Learning?

def display_message()->str:
    '''prints the message "I am learning about functions in Python"'''
    print("I am learning about functions in Python")

display_message()


# Exercise 2: What's Your Favorite Book?

def favorite_book(title)->str:
    '''prints 'One of my favorite books is...' using the input provided'''
    print(f'One of my favorite books is {title}')

favorite_book("Alice in Wonderland")


# Exercise 3: Some Geography

def describe_city(city, country='Unknown')->str:
    '''prints message "{city} is in {country}"'''
    print(f'{city} is in {country}')

describe_city('Buenos Aires', 'Argentina')
describe_city('Montevideo', 'Uruguay')
describe_city('Mitzpe Ramon', 'Israel')
describe_city('Paris')


# Exercise 4 - Random

def random_number(num)->str:
    '''creates a random number and checks if the input is equal to or different from it
    if equal, prints 'Success!' message
    if different, prints 'Fail' the random num and input num'''
    if num in range(1,101):
        random_num = random.randint(1,100)
        if num == random_num:
            print('Success!')
        else:
            print(f'Fail! Your number: {num}, Random number: {random_num}')
    else:
        print('You provided a number that\'s not in range 1-100')


# Exercise 5: Let's Create Some Personalized Shirts!

def make_shirt(size='large', text='I love Python')->str:
    '''prints the size of input shirt and custom message'''
    print(f'The size of the shirt is {size} and the text is {text}')

make_shirt()
make_shirt('medium')
make_shirt('small', 'I love Miami')
make_shirt(size='small', text='Hello!')


# Exercise 6: Magicians...

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(list):
    for magician in list:
        print(magician)

show_magicians(magician_names)

def make_great(list):
    for index, magician in enumerate(list):
        list[index] = magician + ' ' + 'the Great'

make_great(magician_names)
show_magicians(magician_names)


# Exercise 7: Temperature Advice

def get_random_temp()->float:
    '''
    generates a random temperature
    '''
    random_temp = round(random.uniform(-10,40),1)
    return random_temp

def main()->str:
    '''
    prints current temperature using get_random_temp
    prints advice based on the temperature returned 
    '''
    random_temperature = get_random_temp()
    print(f'The temperature right now is {random_temperature} degrees Celsius')
    if random_temperature < 0:
        print('Brrr, that’s freezing! Wear some extra layers today.')
    elif 0 <= random_temperature <= 15:
        print('Quite chilly! Don’t forget your coat.')
    elif 16 <= random_temperature <= 23:
        print('Nice weather.')
    elif 24 <= random_temperature <= 32:
        print('A bit warm, stay hydrated.')
    elif random_temperature >= 32:
        print('It\'s really hot! Stay cool.' )

main()

# Bonus

def get_random_temp()->int:

    '''
    Prompts the user to enter a month number 
    calculates season based on month 
    returns temperature number based on season
    '''


    # Get valid month input 
    while True: 
        try:
            month_input = input('Enter a month number between 1-12:\n')
            month_input = int(month_input)

            if 1 <= month_input <= 12:
                break
            else: 
                print('Invalid input: Month number must be between 1 and 12. Please try again.')

        except ValueError:
            # Errors when int() conversion fails (user types text)
            print('You entered an invalid number.')
            continue
    
    season = ''
    random_temp = 0
    
    if month_input in range(6,10):
        season = 'summer'
        random_temp = random.randint(25,40)
    elif month_input in range(10,12):
        season = 'autumn'
        random_temp = random.randint(15,28)
    elif month_input == 12 or month_input in range(1,3):
        season == 'winter'
        random_temp = random.randint(5,18)
    elif month_input in range(3,6):
        season == 'spring'
        random_temp = random.randint(15,30)
    
    return random_temp

def main()->str:
    '''
    prints current temperature using get_random_temp
    prints advice based on the temperature returned 
    '''
    random_temperature = get_random_temp()
    print(f'The temperature right now is {random_temperature} degrees Celsius')
    if random_temperature < 0:
        print('Brrr, that’s freezing! Wear some extra layers today.')
    elif 0 <= random_temperature <= 15:
        print('Quite chilly! Don’t forget your coat.')
    elif 16 <= random_temperature <= 23:
        print('Nice weather.')
    elif 24 <= random_temperature <= 32:
        print('A bit warm, stay hydrated.')
    elif random_temperature >= 32:
        print('It\'s really hot! Stay cool.' )

main()