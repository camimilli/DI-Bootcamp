# DUNDER METHODS 
# Also known as magic/special methods 
# D = double / UNDER - underscore
# We don't need to call dunder methods (like __init__)
# used to have fast information/actions on the class/instances
# we write them at the end of the class (except __init__)
# there are MANY dunder methods available to use (e.g: dunder method that allow comparison) 

########################################

# __init__ (we know it)

########################################

# __str__
# provides a string representation of an object
# primarily intended for display to a user 

class Person:

    # class attribute 
    id_number = 1 

    def __init__(self, name, last_name, birth_date, age):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.age = age 
        Person.id_number += 1 # this increments the id_number every time a person is created 
        # acces
        # s class attribute -> Class.attribute 

    def __str__(self):
        return f'name: {self.name} \nlast name: {self.last_name}\nbirth date: {self.birth_date}' 

# __repr__
# to give information to the developer - mainly for backend 
# is not intended for user display (frontend) like __str__ is 
# if we print an object like print(p1) and there's no __str__ method, the __repr__ will be used 


    def __repr__(self):
        return f'{self.__dict__}'
    
# comparison 
# there are dunder methods that allow us to compare between two objects 

    def __lt__(self, other):
        return self.age < other.age 
    
    def __eq__(self, other): # equal
        return self.age == other.age 


p1 = Person('John', 'Snow', '21-08-1990', 20)
p2 = Person('Camila', 'Millicovsky', '27-03-1995', 30)
p3 = Person('Niv', 'Yakir', '08-10-1994', 30)
print(p1) # this is how __str__ is used, instead of printing the object memory it will print what we specified in the __str__ dunder method
print(repr(p1)) # this is how I get the info from __repr__ in case there's also a method __str__ in the code
print(p1 > p2) # used __lt__ method for < comparison operator
print(p3 == p3) # used __eq__ method for == comparison operator