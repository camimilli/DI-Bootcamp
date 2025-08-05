# Exercise 3: Dogs Domesticated 

import random
from Exercise2 import Dog

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
        random_index = random.randint(0,len(tricks))
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



