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
            try:
                print(animal.walk())
            except AttributeError:
                print(f"I can't walk a {type(animal).__name__} object because it doesn't have a 'walk' method")
   

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


all_cats = [Bengal("Bengal", 2), '123', 2] #[Bengal("Bengal", 2), Chartreux("Chartru", 5), Siamese("Cinco", 7)]
sara_pets = Pets(all_cats)
sara_pets.walk()
# print(all_cats[2].dance('boogie'))


# Exercise 2: Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight 

    def bark(self)->str:
        '''
        Returns a string of 
        '{self.name} is barking'
        '''
        return f'{self.name} is barking'
    
    def run_speed(self)->int:
        '''
        returns the result of the dog's run speed 
        weight / age * 10 
        '''
        return self.weight / self.age * 10
    
    def fight(self, opponent:object)->str:
        '''
        compares the object's weight*run_speed() 
        with the argument passed (opponent)
        and returns a string based on who won / if it's a tie
        '''
        if (self.weight * self.run_speed()) > (opponent.weight * opponent.run_speed()):
            return f'{self.name} won the fight against {opponent.name}'
        elif (self.weight * self.run_speed()) == (opponent.weight * opponent.run_speed()):
            return f'IT\'S A TIE!'
        else:
            return f'{opponent.name} won the fight against {self.name}'


dog1 = Dog('Mushu', 5, 19)
dog2 = Dog('Luna', 4, 25)
dog3 = Dog('Bigote', 2, 5)

print(dog1.bark())
print(dog2.run_speed())
print(dog3.fight(dog2))


# Exercise 3: Dogs Domesticated 

import random

class PetDog(Dog):

    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained 

    def train(self):
        '''
        calls and prints output of bark() function
        sets trained attribute to True 
        '''
        print(self.bark())
        self.trained = True 

    def play(self, *args)->str:
        '''
        Accepts an indefinite amount of args 
        prints the self name, the args and 
        'All play together' 
        '''
        for dog in args:
            print(dog, sep=', ')
        print(self.name)
        print('All play together')

    def do_a_trick(self)->str:
        '''
        Check if dog is trained 
        if yes -> returns a string showing dog doing random trick 
        if not -> returns a string saying the dog is not trained with no tricks
        '''
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        random_index = random.randint(0,len(tricks)-1)
        if self.trained == True:
            print(f'{self.name} {tricks[random_index]}')
        else:
            print(f'{self.name} is not trained, it doesn\'t know how to do any tricks :(')


my_dog1 = PetDog('Mushi', 3, 40)
my_dog2 = PetDog('Mimi', 5, 10, True)
my_dog1.do_a_trick()
my_dog1.train()
my_dog1.do_a_trick()
my_dog3 = PetDog('Laila', 1, 15)
my_dog3.do_a_trick()
my_dog1.play('Buddy', 'Max', 'Peter')

# Exercise 4: Family And Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age 
        self.last_name = ''

    def is_18(self)->bool:
        '''
        Check if the person is above or below 18 
        '''
        if self.age >= 18:
            return True
        else:
            return False 
        
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        '''
        Creates a new instance from class Person 
        adds the new member to the members list
        '''
        new_member = Person(first_name, age)
        self.members.append(new_member)

    def check_majority(self, first_name)->str:
        '''
        Checks if the member exits in members list
        if yes -> checks if over or under 18 and checks if they can go out with friends
        if not -> returns that person is not part of members list 
        '''
        
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print('You are over 18, your parents Jane and John accept that you will go out with your friends')
                else:
                    print('Sorry, you are not allowed yo go out with your friends.')
                return 
        
        print(f'{first_name} is not a member of the {self.last_name}\'s family')
        

    def family_presentation(self)->str:
        '''
        Returns family last name 
        followed by members' first name and age 
        '''
        print(self.last_name)
        for family_member in self.members:
            print(f'{family_member.first_name} {family_member.age} years old')


millicovsky = Family('Millicovsky')
millicovsky.born('Gisela', 39)
millicovsky.born('Camila', 30)
millicovsky.born('Susana', 74)
millicovsky.born('Leonardo', 80)
millicovsky.born('Alba', 1)
millicovsky.check_majority('Camila')
millicovsky.check_majority('Alba')
millicovsky.check_majority('Mateo')
millicovsky.family_presentation()