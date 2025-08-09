# TRY AND EXCEPT BLOCK 
# Exception - error that crashes our program 
# ERROR HANDLING - Try-except handle errors so the program doesn't crash 
# with a while loop we can do it again and again 

# ERROR TYPES 
# can take a look at built in exceptions in Python documentation
# Common errors: 
#           - SyntaxError - something in the syntax is wrong (like, forgot a : on a function)
#           - NameError - I use a name that's not defined 
#           - IndexError - Trying to access an index in a list that doesn't exist
#           - KeyError - Trying to access a key that doesn't exist 
#           - ZeroDivisionError - Trying to divide by zero 

# we add while True, to keep asking for input until input correct 

while True:
    try:
        # ask for input, we put float instead of int, in case user gives a float
        move = float(input('Give ur move from 1 - 9: '))
        # we convert to int by rounding the float
        move = round(move)

        # this happens only if the user enters a float and we can round it (step before succesfull)
        if move not in range(1,10):
            raise Exception('Choose a number in range 1 - 9: ')
        
        # if succesfull 
        
        print('thank you for the right input')
        break # we got the right answer

    #if the error happens on the first line under try, the program will go to except block

    except Exception as e: # we use this, exception as e, so python returns the error that happened (will be most accurate)
        # except: 
            # print('you entered a letter') -> we can use this for a custom message
        print(e) # e is the error, in this case will be "ValueError: Invalidad literal..."
        
        # the continue asks again for input 
        continue 
    finally: # everything you put after this happens no matter what (if error, not error)
        # used a lot for connecting with database after finishing giving/retrieving information where we need to close the connection
        print('finally message')

########################################

while True:
    try:
        age = int(input('what is your age? '))
        10/age 
    except ValueError: # this runs if the exception raised is ValueError
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you!')
        break 