# Exercise 2: Dogs

class Dog:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high!')


def compare_size(dog_1, dog_2):

    if dog_1.height > dog_2.height:
        print(f'{dog_1.name} is higher than {dog_2.name} by {dog_1.height - dog_2.height} cms!')

    elif dog_2.height > dog_1.height:
        print(f'{dog_2.name} is higher than {dog_1.name} by {dog_2.height - dog_1.height} cms!')

    else:
        print(f'{dog_1.name} and {dog_2.name} have the same height')


davids_dog = Dog('Fluffy', 10)
sarahs_dog = Dog('Pirate', 20)

print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()
compare_size(davids_dog,sarahs_dog)

