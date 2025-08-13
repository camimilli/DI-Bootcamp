# Create an @authenticated decorator that only allows the function to run
# if user1 has 'valid' set to True:

user1 = {
    'name': 'Sorna',
    'valid': False # changing this will either run or not run the message_friends function
}

def authenticated(fn):

    def wrapper(*args, **kwargs): 
        if args[0]['valid']: #accessing element 0 from the tuple (as dict is passed as positional argument) and then getting access to 'valid' key value
            fn(*args, **kwargs)
        else:
            print(f'{user1['name']} is not authenticated and can\'t send a message, validate them and try again') 
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)