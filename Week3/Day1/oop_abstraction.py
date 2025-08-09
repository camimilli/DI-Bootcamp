# ABSTRACTION = Hiding of information and giving access only when needed, prevents direct changes on attributes/methods.
# Python doesn't have a way to define private attributes, it uses name convention and name mangling. 
#   Single underscore prefix (_) - Indicates an attribute/method should be treated as "protected" or "internal" - hints other programmers 
# that they shouldn't access it directly from outside the class but Python will not stop them if they do.

#   Double underscore prefix (__) - Stronger convention that uses name mangling to make the attribute harder to access accidentally. It changes the name of the attribute/method
# behind the scene so when calling for the method/attribute causes an error because the attribute/method is not found (as the name was "changed") but can be worked around if you know the mangling name.

########################################

class Computer():

    def __init__(self):
        self.name = 'Apple Computer' # public
        self.__max_price = 900 # private 
        # we won't be able to access __max_price attribute by doing object.__max_price as it's private
        # you can only access it with the sell() method

    def sell(self): # public method
        print(f'Selling price: {self.__max_price}')

    def __sell(self): # private method
        print('This is a private method')

    def set_max_price(self, price):
        self.__max_price = price 

c = Computer()

# change the price - won't do anything 
# get error 
c.__max_price = 1000 
c.sell()

# right way to change the price using set function
c.set_max_price(1000)
c.sell()
# Selling Price: 1000 

########################################

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name # _name or _age let devs this attribute shouldn't be modified (it's private)
                          # but Python doesn't prevent you from modifying these attributes if you try
        self._age = age 

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('andrei', 100)
player1.speak()

# OVERWRITING OBJECTS / METHODS OF A CLASS 🤯
# We can just change the name of player1 and even the method of speak()
# THAT'S BAD! we don't want any programer to come and overwrite our hard work
# player1.name = '!!!'
# player1.speak = 'BOOOO'
# print(player1.speak()) # will give an error because the method has been changed to BOOO! 

