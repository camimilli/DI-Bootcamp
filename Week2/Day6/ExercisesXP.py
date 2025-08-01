# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name 
        self.age = cat_age 

    def oldest(self, cat1, cat2):
        oldest = ''
        if self.age > cat1.age and self.age > cat2.age:
            oldest = self
        elif cat1.age > self.age and cat1.age > cat2.age:
            oldest = cat1
        else:
            oldest = cat2
        print(f'The oldest cat is {oldest.name} and is {oldest.age} years old')        


cat_one = Cat('Silki', 3)
cat_two = Cat('Napoleon', 10)
cat_three = Cat('Sparrow', 6)
Cat.oldest(cat_one, cat_two, cat_three)


# Exercise 2: Dogs
