import random 

# Exercise 1: When Will I Retire?

current_year = 2025
current_month = 7
current_day = 29

def convert_date(date)->int:
    '''
    converts a birthdate into its separate components:
    - year
    - month 
    - day
    '''
    birthdate = date.split('/')
    for index in range(len(birthdate)):
        if index == 0:
            pass 
        else:
            if len(birthdate[index]) == 2 and birthdate[index][0] == '0':
                birthdate[index] = birthdate[index][1].replace('0','')
    
    birthdate = [int(date_component) for date_component in birthdate]
    
    year = birthdate[0]
    month = birthdate[1]
    day = birthdate[2]
    return year, month, day


def get_age(year, month, day)->int:
    '''
    Returns the age of a person 
    based on their birthdate 
    '''
    age = current_year - year
    if current_month < month:
        age -= 1 
    elif current_month == month:
        if current_day < day:
            age -= 1
    return age 


def can_retire(gender, date_of_birth)->str:
    '''
    Determines if a person can retire based on their gender and date of birth
    Retirement age: 67 for men, 62 for women
    '''

    # convert birthdate to int and unpack values 
    year, month, day = convert_date(user_birthdate)
    age = get_age(year, month, day)
    if (age > 67 and gender == 'm') or  (age > 62 and gender =='f'):
        print('You reached retirement age, congrats!')
    else:
        if gender == 'm':
            print(f'You still have {67-age} years to retire')
        elif gender == 'f':
            print(f'You still have {62-age} years to retire')

while True: 
    try:
        user_gender = input("Enter your gender, write 'm' for male / 'f' for female:\n")

        if user_gender == 'm' or user_gender == 'f':
            break
        else: 
            print("You're only allowed to enter 'm' or 'f'.") 

    except Exception as e:
        # This catches any other unexpected errors
        print("An unexpected error ocurred.")

user_birthdate = input("Enter your date of birth in the form of 'YYYY/MM/DD':\n")


can_retire(user_gender, user_birthdate)


# Exercise 2: Sum

def sum_increment(x)->int:
    '''
    Calculates the sum of X + XX + XXX + XXXX, where X, XX, XXX, XXXX
    are formed by repeating the digit(s) of the input integer X.
    '''
    num_increment = x 
    sum = 0
    for num in range(1,5):
        num_increment = int(num_increment)
        sum += num_increment
        num_increment = str(num_increment)
        num_increment += str(x)
    return sum

print(sum_increment(3))


# Exercise 3: Double Dice

def throw_dice()->int:
    '''
    generates a random number from 1-6
    returns that numbers
    '''
    random_number = random.randint(1,6)
    return random_number

def throw_until_doubles():
    '''
    throws doubles until they are both equal 
    '''
    counter = 0
    while True:
        dice_one = throw_dice()
        dice_two = throw_dice()
        counter +=1 
        if dice_one == dice_two:
            break
    return counter 

def main():
    counter_100 = 0
    throws_per_iteration = []
    double_counter = 0
    while counter_100 != 100:
        double_counter = throw_until_doubles()
        throws_per_iteration.append(double_counter)
        counter_100 += 1 
    average_throws_100 = round(sum(throws_per_iteration)/len(throws_per_iteration),2)
    print(f'Total throws to reach 100 doubles: {sum(throws_per_iteration)}\nAverage throws to reach doubles: {average_throws_100}')


main()
        



    













