# CLASS ATTRIBUTES
# Attributes that belong to the class and not to each instance
# Every instance in the class shares the same class attribute

# EXAMPLE 1


class Employee: 

    # class variable 
    num_of_emps = 0
    raise_amount = 1.04 


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1 

    def fullname(self)->str:
        '''
        Returns full name of employee 
        '''
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # we use self to make sure that we can use a unique attribute if we want to 
        # but also the class variable if the object doesn't have a unique raise amount value 
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(Employee.num_of_emps)
emp_3 = Employee('Camila', 'Millicovsky', 400000)
print(Employee.num_of_emps)


# EXAMPLE 2
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


# EXAMPLE 2

class Dog():

    # Class attributes 
    number_of_dogs = 0
    dogs_king = "Bernie IV"

    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is ", name_of_the_dog)
        self.name = name_of_the_dog
        # incrementing class attribute number_of_dogs every time an object is initiated
        Dog.number_of_dogs += 1 

    def bark(self):
        print(f"{self.name} barks ! WAF")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def rename(self, new_name):
        self.name = new_name

my_dog = Dog("Rex")
my_dog.rename("Paul")

# Accessing class attribute 
print("The king of the dogs is: ", Dog.dogs_king)
print(f"Currently there are {Dog.number_of_dogs} dogs")

