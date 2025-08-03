# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name 
        self.age = cat_age 

def oldest(cat1, cat2, cat3):
    oldest = ''
    if cat1.age > cat2.age and cat1.age > cat3.age:
        oldest = cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        oldest = cat2
    else:
        oldest = cat3
    print(f'The oldest cat is {oldest.name} and is {oldest.age} years old')        


cat_one = Cat('Silki', 3)
cat_two = Cat('Napoleon', 10)
cat_three = Cat('Sparrow', 6)
oldest(cat_one, cat_two, cat_three)