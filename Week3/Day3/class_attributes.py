# CLASS ATTRIBUTES - attributes that belong to the class (not to confuse with instance attributes)

class Person:

    # class attribute 
    id_number = 1 

    def __init__(self, name, last_name, birth_date):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        Person.id_number += 1 # this increments the id_number every time a person is created 
        # access class attribute -> Class.attribute 

p1 = Person('John', 'Snow', '21-08-1990')
print(Person.id_number) # id_number of class went up by 2 because we created a new person so it went up by 1 

