# Daily Challenge: Old MacDonald's Farm

class Farm:

    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animals(self, animal_type, count=1)->dict: # args
        '''
        Adds animals to the farm 
        '''
        if animal_type in self.animals.keys():
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

        return self 
    
    def get_info(self)->str:
        '''
        returns a string that displays: 
        - farm name 
        - animals + counts
        - E-I-E-I-O! phrase 
        '''
        farm_name = f'{self.name}\'s farm \n\n'
        
        for key, value in self.animals.items():
            farm_name += f'{key}: {value}\n'
        farm_name += '\nE-I-E-I-O!'

        return farm_name

    def get_animals_type(self):
        sorted_animals = sorted(self.animals) 
        return sorted_animals
    
    def get_short_info(self):
        animals = []

        for animal in self.get_animals_type():
            if self.animals[animal] > 1:
                animals.append(animal+'s')
            else:
                animals.append(animal)
            
        return f"{self.name}'s farm has " + ", ".join(animals)

       

mcdonals_farm = Farm('McDonals')
mcdonals_farm.add_animals('cow', 5) 
# add *args and update call method ('cow', 'sheep', 'goat'...) 
# check how to pass numbers
mcdonals_farm.add_animals('sheep')
mcdonals_farm.add_animals('sheep')
mcdonals_farm.add_animals('goat', 12)
print(mcdonals_farm.get_info())
print(mcdonals_farm.get_animals_type())
print(mcdonals_farm.get_short_info())
    