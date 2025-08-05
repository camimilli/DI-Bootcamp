# INHERITANCE: Parent and child 

class Parent:
    def speak(self):
        print(f'Parent speaking')


# CREATING A CHILD CLASS 
# Add Parent class in between () when defining child class

class Child(Parent): 
    def speak(self):
        print(f'Child Speaking')
# logic of inheritance goes up through generation and brings back the FIRST one it founds
# so, because Child has a method called "speak" that's same as the Parent but more recent, 
# the child and the grandchild use the one from Child 
# the closest method in generation is the one that will be called 


class Grandchild(Child):
    pass 

# obj1 = Child()
# obj1.speak() # obj1 from Child class can use Parent class methods as "Inherits" them

# obj2 = Grandchild()
# obj2.speak() # uses the Child speak() method, not the Parent


class Animal: 

    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs 

    def sleep(self):
        return f'{self.name} is sleeping - from Animal'

class Dog(Animal):
    # creating attributes BESIDES the ones inherited from Animal 
    # need to pass all the Animal __init__ attributs 
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs) # instead of writing self.name again, we use super().__init__() and pass the arguments 
        self.trained = trained               # that will come from the parent (Animal)
        self.age = age 
        
# super() is a new feature, before it was used as Parent.__init__() (Parent is name of Parent class)

    def bark(self):
        return f'{self.name} is barking'

class Cat(Animal):
    def __init__(self, name, family, legs, friendly, age, nickname):
        super().__init__(name, family, legs) # instead of writing self.name again, we use super().__init__() and pass the arguments 
        self.friendly = friendly               # that will come from the parent (Animal)
        self.age = age   
        self.nickname = nickname  

    def get_crazy(self):
        if self.friendly:
            return f'{self.name} doesn\'t get crazy'
        else:
            return f'{self.name} is running in full power'

########################################

# MULTIPLE INHERITANCE 

class Alien:
    def __init__(self, name, planet):
        self.personal_name = name
        self.planet = planet 

    def bark(self):
        return f'{self.name} goes Ululululu'

# The order in the () MATTERS because of the methods 
# the order of the inherited classes define which methods will inherit first 
# you can also use the class.method(object) syntax

class AlienDog(Alien, Dog):
    # what would happen if we have same attribute name that comes from two different inhereted classes? ⬇️
    # here we have name attribute, but we have name in Dog and Alien class. 
    # meaning, if we call the name from the Alien or Dog it will be recognized as the same value 
    def __init__(self, name, family, legs, trained, age, planet): # the attributes order passed is not important for the code to run but it's important for readability (first the ones from the first class then the other class)
        Alien.__init__(self, name, planet)
        Dog.__init__(self, name, family, legs, trained, age)
        # if we use super().__init__ we need () because it's a function
        # when we use the class Name we don't need () 

dog1 = Dog('Rex', 'Canine', 4, True, 5)
print(dog1.bark())
print(dog1.sleep())
cat1 = Cat('Fluffy', 'Feline', 4, False, 10, 'Fluff')

alien_dog1 = AlienDog('Buba', 'Canine', 6, True, 135, 'Jupiter')
print(alien_dog1.bark()) # the bark comes from the Alien class because in the parentheses
                         # of AlienDog the class from which the alien_dog1 belongs to 
                         # it has Alien as the first class
                         # the order of the inherited classes define which methods will inherit first 


# Specifying from which class I want the method to be called from
print(Dog.bark(alien_dog1))

########################################

# EXERCISE 
# Create an AlienCat class that inherits from Cat and Alien.
# create a method fly_away that calls the method get_crazy, prints its output 
# and adds 'as an alien cat'

class AlienCat(Cat, Alien):
    # if I don't define an __init__ for AlienCat and pass all the attributes
    # which are self, name, family, legs, friendly, age, planet
    # it will take the attributes from the FIRST class (Cat) but if you pass 
    # an argument when creating an object (like the planet) then it won't allow you to create the object

    def fly_away(self):
        return f'{self.get_crazy()} as an alien cat'
    
alien_cat1 = AlienCat('Pirate', 'Feline', 7, False, 234, 'Pats')
print(alien_cat1.fly_away())


########################################

# POLYMORPHYSM = to "have many forms or faces"

# When we have a Parent and a Child class connected 
# and you override the Parent's method with the Child's method 
# you override it by calling the method the same name on both classes 

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod 
    def area(self):
        pass  

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return 3.14 * self.radius ** 2 

class Square(Shape):
    def __init__(self, side):
        self.side = side 

    def area(self):
        return self.side ** 2 

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base 
        self.height = height  

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(4), Square(5), Triangle(6,7), Pizza('pepperoni', 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")



