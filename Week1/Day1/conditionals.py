print(5 > 8)
print(5 > 3)

#CONDITIONALS 

#SYNTAX 
#if <condition>:
#    action

if 5 > 3 :
   print('Hello world')  
else:
   print('Not Hello')

age = int(input('Age?'))

if age <= 18:
   print('Sorry, you can\'t watch the movie')
elif age == 21:
   print('You got a free popcorn!')
else:
   print('You can watch the movie')

#exercise 2
user_name = input('Name?')

if len(user_name) < 5 and user_name[0] == 'R':
   print('you have a short name and it starts with "R" ')