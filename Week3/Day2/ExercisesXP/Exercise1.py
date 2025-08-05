# Exercise 1: Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals 

    def walk(self)->str:
        '''
        iterates through the list of animals from the object
        and activates the method walk from the animal class 
        '''
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def walk(self)->str:
        '''
        returns a string of "{name} is just walking around"
        '''
        return f'{self.name} is just walking around'
    
class Bengal(Cat):
    def sing(self, sounds)->str:
        '''
        returns cat's sounds
        '''
        return f'{sounds}'
    
class Chartreux(Cat):
    def sing(self, sounds)->str:
        '''
        returns cat's sounds 
        '''
        return f'{sounds}'

class Siamese(Cat):
    def dance(self, move)->str:
        '''
        returns a string with object's name and move 
        '''
        return f'{self.name} is doing the {move} with elegance'


all_cats = [Bengal("Bengal", 2), Chartreux("Chartru", 5), Siamese("Cinco", 7)]
sara_pets = Pets(all_cats)
sara_pets.walk()
print(all_cats[2].dance('boogie'))
