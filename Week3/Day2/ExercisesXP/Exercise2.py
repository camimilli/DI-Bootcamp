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
    
    def fight(self, other_dog)->str:
        '''
        compares the object's weight*run_speed() 
        with the argument passed (other_dog)
        and returns a string based on who won / if it's a tie
        '''
        if (self.weight * self.run_speed()) > (other_dog.weight * other_dog.run_speed()):
            return f'{self.name} won the fight against {other_dog.name}'
        elif (self.weight * self.run_speed()) == (other_dog.weight * other_dog.run_speed()):
            return f'IT\'S A TIE!'
        else:
            return f'{other_dog.name} won the fight against {self.name}'

if __name__ == "__main__":
    dog1 = Dog('Mushu', 5, 19)
    dog2 = Dog('Luna', 4, 25)
    dog3 = Dog('Bigote', 2, 5)

    print(dog1.bark())
    print(dog2.run_speed())
    print(dog3.fight(dog2))