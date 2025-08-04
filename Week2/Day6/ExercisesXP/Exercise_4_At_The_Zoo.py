# Exercise 4: Afternoon At The Zoo

class Zoo:

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

        return self 
    
    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} can't be sold, it doesn't belong to {self.zoo_name}")
            
        return self 
    
    def sort_animals(self):

        first_letter = set(animal[0] for animal in self.animals)
        first_letter = list(first_letter)
        first_letter.sort()

        grouped_animals = {letter:[] for letter in first_letter}

        for letter in first_letter:
            for animal in self.animals:
                if letter == animal[0]:
                    grouped_animals[letter].append(animal)

        return grouped_animals
    
    def get_groups(self):
        print(self.sort_animals())


israel_safari = Zoo('Safari Israel')

israel_safari.add_animal('Giraffe')
israel_safari.add_animal('Bear')
israel_safari.add_animal('Baboon')
israel_safari.add_animal('Hipo')
israel_safari.add_animal('Elephant')
israel_safari.add_animal('Hiena')
print(israel_safari.animals)

israel_safari.sell_animal('Giraffe') 

israel_safari.sell_animal('Zebra') 
israel_safari.get_animals()

israel_safari.sort_animals()
israel_safari.get_groups()