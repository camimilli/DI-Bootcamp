def get_short_info(self):
    animals_in_farm = f'{self.name} farm has'
    s = "'s"

    for key, animal in self.get_animals_type():
        if self.animals[animal] > 1:
            animals_in_farm += f' {animal}{s}, '
        else:
            animals_in_farm += f' {animal}'
        
    return animals_in_farm

