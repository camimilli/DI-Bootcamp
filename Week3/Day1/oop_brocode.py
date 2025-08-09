# # class Animal:
# #     def __init__(self, name):
# #         self.name = name 
# #         self.is_alive = True 

# #     def eat(self):
# #         print(f'{self.name} is eating')

# #     def sleep(self):
# #         print(f'{self.name} is asleep')

# # class Dog(Animal):
# #     def speak(self):
# #         print(f'WOOF!') 

# # class Cat(Animal):
# #     def speak(self):
# #         print(f'MEOW!') 

# # class Mouse(Animal):
# #     def speak(self):
# #         print(f'SQUEEK!') 

# # dog = Dog('Scooby')
# # cat = Cat('Garfield')
# # mouse = Mouse('Mickey')

# # dog.speak()
# # cat.speak()
# # mouse.speak()

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} is eating')

#     def sleep(self):
#         print(f'{self.name} is sleeping')


# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting") 

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass 

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")

# rabbit.eat()
# rabbit.sleep()
# hawk.hunt()
# fish.hunt()


# Abstract class 
# template for other classes. It defines methods that MUST be included in any class that inhertis from it 
# but it doesn't provide the actual code for those methods. 

# abs - abstract base classes need it for abstract classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass 

    @abstractmethod
    def stop(self):
        pass 

# if you try to create an object from an abstract class 
# it won't let you - try running code :) 
# vehicle = Vehicle()

# class that inherits from abstract parent with abstract methods
# we HAVE to define those methods in the child class 
class Car(Vehicle):
    
    def go(self):
        print("You drive the car") 

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):
    
    def go(self):
        print("You drive the motorcycle") 

    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):

    def go(self):
        print('You sail the boat')

    def stop(self):
        print('You anchor the boat')

boat = Boat()
boat.go()
boat.stop()


# super() = Function used in a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color 
        self.is_filled = is_filled 

    def describe(self):
        print(f"It is {self.color} and is {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius): 
        super().__init__(color, is_filled)
        self.radius = radius 

    # method overwritting - if the parent has the same method
    # and the child has a method with the same name, python will use the child's method and override the parent's method
    def describe(self):
        # if I want to use BOTH methods, I can use the super() method to EXTEND the functionality of this method
        # can be at any place, at the end or at the beginning of the method
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius} cm²")
        
        

class Square(Shape):
    def __init__(self, color, is_filled, width): 
        super().__init__(color, is_filled)
        self.width = width 

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm²")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height): 
        super().__init__(color, is_filled)
        self.width = width
        self.height = height 

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm²")
        super().describe()

circle = Circle(color = 'red', is_filled = True, radius = 5)
print(circle.color)
print(circle.is_filled)
print(f'{circle.radius}cm')

circle.describe()

square = Square(color = 'blue', is_filled = False, width = 6)
print(square.color)
print(square.is_filled)
print(f'{square.width}cm')

square.describe()

triangle = Triangle(color = 'yellow', is_filled = True, width = 7, height = 8)
print(triangle.color)
print(triangle.is_filled)
print(f'{triangle.width}cm')
print(f'{triangle.height}cm')

triangle.describe()


# Polymorphism = Greek word that means to "have many forms or faces"

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods



      