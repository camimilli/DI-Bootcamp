# FUNCTIONS AND STRUCTURES

# EXERCISE 1 
# create a function called welcome() that says Name, welcome to Hogwarts 
# for each one of the students of the given list

students = ['Harry', 'Ron', 'Hermione']

def welcome(): # don't need to pass the list students as it's a global variable 
    for name in students:
        print(f'{name}, welcome to Hogwarts!')

welcome() # don't need to pass the list students as it's a global variable 

# IMPORTANT - modifying global list items 
def get_house(): # we don't need to pass the list even if we're modifying it because we're redifiying by index
    for index, name in enumerate(students):
         students[index] = f'{name} - Griffyndor'

get_house()
print(students)

