# CLASS DECORATORS - 
# built-in decorators:
#   @classmethod, @staticmethod, @property
# decorators are function that change the default function behavior 
# you can build your own decorators (advanced)

########################################

# @staticmethod
# method in the scope of the class that doesn't need 'self'
# e.g - used when you need to parse something (like age, birthdate) as you don't need the object itself 
# e.g - in a bank account, someone passes a float, a static method can convert float to int 
# e.g - checking different currencies and the person passed USD info and you need to parse it to shekel you can use staticmethod 

from datetime import datetime, date

class Person:

    id_number = 1 

    def __init__(self, name, last_name, birth_date):
        self.name = self.format_name(name)
        self.last_name = self.format_name(last_name)
        self.birth_date = self.parse_birthdate(birth_date) # passing static method !!with self!!
        Person.id_number += 1 
        

    # @staticmethod
    # call staticmethod of parse_birthdate on __init__ method 
    # to automatically convert the birth_date into the right format
    @staticmethod 
    def parse_birthdate(date_str):
        # datetime.strptime(value, format) - formats string into time format 
        # the format is how you're passing the date, if I have '21-08-1990' I need to pass it '%d-%m-%Y'
        return datetime.strptime(date_str, '%d-%m-%Y').date() # we put .date() because we only need the date, not the hours
         
# EXERCISE 
# create a static method that format the name and last name 
# in case the first letter is not upper case use .upper()

    # very useful method as most data will come from forms
    # and we'll need to format that data 
    @staticmethod
    def format_name(name):
        if not name[0].isupper():
            return name.capitalize()
        else:
            return name

# @classmethod 
# method related to the class, not to the object
# instead of passing "self" we pass "class"
# can be called before object is initiated (see on prints)

    @classmethod
    def from_age(cls, name, last_name, age):
        '''
        calculates in wich year the person was born 
        taking into consideration their birthday is on 1st of January
        is just for giving an example for classmethod 
        '''
        current_year = datetime.today().year
        birth_year = current_year - age 
        birth_date = f'1-1-{birth_year}' # we make a string because after that the __init__ for birthdate has a parsing method
        return cls(name, last_name, birth_date) 


# @property
# To add a property (attribute) without changing the __init__ 
# Sometimes used after you created 100 objects and you realize you need to add another property
# if you'd add it to __init__ with default value it can break logics you already wrote in your code 
# if you add it to __init__ with no default value, then it will create errors because the objects you created don't have that attribute 

    @property
    # name of the function needs to be name of the property we will create
    # we need self because we're changing instances
    # it will add the age attribute with the right value to all the objects that were created from the Person class
    def age(self): 
        today = date.today()
        age = today.year - self.birth_date.year 
        return age 


p1 = Person('John', 'Snow', '21-08-1990')
print(datetime.today()) # datetime.today gives today's date 
print(datetime.strptime('21-08-1990', '%d-%m-%Y').date())
p2 = Person('camila', 'millicovsky', '27-03-1995')
print(Person.format_name('camila')) # I can check with a string without passing an object, as I'm not using self 
print(p2.name, p2.last_name, p2.birth_date)

# Calling the class method before initializing object
p3 = Person.from_age('niv', 'yakir', 30) 
print(p3.birth_date)

# using the @property age method 
# It doesn't automatically run when you create the method 
# it runs when you call the attribute 
print(p2.age)
print(p1.age)




