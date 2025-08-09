# POLYMORPHYSM - poly = many / morph = forms
# The idea that object classes can share the same method name but those method names cna act differently
# based on what object calls the method

class User(object):
    pass 

class Wizard(User):
    def __init__(self, name, power):
        self.name = name 
        self.power = power 

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

def player_attack(char):
    char.attack()

# when I call the player_attack() function it runs a different attack based on the object I pass, that's polymorphysm
player_attack(wizard1)
player_attack(archer1)

# it also works when we call the char.attack() it will call the object's class method with that name, if it doesn't exist 
# it will go to the parent class and check if that class has a method called attack() 
