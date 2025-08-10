# Exercise 6: Birthday And Minutes

import datetime 

current_time = datetime.datetime.now()
print(current_time)

def birthday_message(birthdate)->str:
    '''
    Returns how many minutes have passed 
    since someone's birthdate 
    '''
    # convert string to datetime object 
    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    
    # calculate minutes alive 
    time_difference_secs = (current_time - birthdate).total_seconds()
    minutes_alive = round(time_difference_secs // 60)
    return f'You\'ve been alive for around {minutes_alive} minutes! How crazy is that?'
    
    
print(birthday_message('1995-03-27'))