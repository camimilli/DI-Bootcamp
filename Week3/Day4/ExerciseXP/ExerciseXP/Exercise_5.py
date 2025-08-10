# Exercise 5: Amount Of Time Left Until January 1st

import datetime 

january_1_2026 = datetime.datetime(2026,1,1)
current_datetime = datetime.datetime.now()

# Calculating time difference 
time_difference =  january_1_2026 - current_datetime

# Accessing time_difference components
days_left = time_difference.days
seconds_left = time_difference.seconds
microseconds_left = time_difference.microseconds

# You can then calculate hours, minutes, and seconds from the 'seconds' attribute
hours_left = seconds_left // 3600 
minutes_left = (seconds_left % 3600) // 60
seconds_final = seconds_left % 60

# Output 
print(f"There's {days_left} days, {hours_left} hours, {minutes_left} minutes and {seconds_final} seconds left until {january_1_2026.date()} at {january_1_2026.time()}")