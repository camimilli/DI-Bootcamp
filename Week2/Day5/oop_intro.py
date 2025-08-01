# OOP = Object Oriented Programming 
# objects belong to a class
# objects are instances of a class 
# objects can have attributes and behaviors or only attributes/behaviors 

########################################
# CLASSES AND OBJECTS 

# How to create a class 
# class name convention - Capitalized 

# class Dog:

#     # the constructor __init__ creates an object when called 
#     def __init__(self, name, color, age, is_trained = False): # self -> the object that will be created + properties of the object 
#         print('The obj is being created') # when we create a new object this function is called so this would be printed if we have it in our code
#         self.name = name 
#         self.color = color 
#         self.age = age
#         self.is_trained = is_trained

# if you created objects and add an attribute to the __init__ without a default value, it will give you an error 
# because your objects have the key but don't have the value
    
# creating object
# dog1 = Dog('Rex', 'Brown', 10)
# dog2 = Dog('Mushu', 'Brown', 5)
# dog3 = Dog('Fluffy', 'white', 2)

# creating a SPECIFIC attribute for a SPECIFIC object 
# if "breed" is not in __init__, other objects won’t have it – useful when only one object needs it
# dog1.breed = 'puddle' 

# Accessing object's properties 
# print(dog1.name)
# print(dog1.color)
# print(dog1.age)

# Accessing object's dictionary __dict__
# print(dog1.__dict__)
# print(dog2.__dict__)

# EXERCISE
# Create a new attribute of the Dog class called "is_trained" the value is a boolean and the default is False
# then run the code again. What happens with the objects that were created before this new attribute was added? 
# answer: the new attribute is added to the object with the default value. 

# type() in class objects
# print(type(dog1)) # <class '__main__.Dog'>

########################################

# BEHAVIOURS = METHODS

# functions + general than methods
# methods = functions related to a certain class - e.g: .capitalize() is a method from the class String
# every function that we want to related to the object we need to pass self 

class Dog:

    #the constructor
    # self = the object that will be created
    def __init__(self, name, color, age, is_trained = False): # self -> the object that will be created + properties of the object 
        self.name = name 
        self.color = color 
        self.age = age
        self.is_trained = is_trained

    def bark(self):
        print(f'{self.name} is barking!!!')

    def run(self):
        if self.age <= 5:
            print(f'{self.name} is running very fast!')
        elif self.age in range(6,10):
            print(f'{self.name} is running')
        else: 
            print(f'{self.name} doesn\'t want to run')

    def walk(self, meters):
        print(f'{self.name} is walking {meters} meters')

    # redefining the value of a propertie
    def rename(self, new_name):
        self.name = new_name 
        return self # best practice to do on methods that change values of attributes

dog1 = Dog('Rex', 'brown', 10)
dog1.bark()
dog1.run()
dog1.rename('Pipito')
Dog.run(dog1) # a different way of calling a method Class.method(object)

# EXERCISE 
# Create a method called walk() that takes a parameter (meters: int) and print "dog"s name is walking (meters) meters"
dog1.walk(200)

# EXERCISE
# Analyse the code below. What will be the output?
# Explain the goal of the methods
# Create a method that modifies the name of the person

class Person:

    # constructor (creates objects)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Person persents itself 
    def show_details(self):
        print("Hello my name is " + self.name)

    def change_name(self, name):
        self.name = name 

first_person = Person("John", 36)
first_person.show_details()
first_person.change_name("Juan")
first_person.show_details()