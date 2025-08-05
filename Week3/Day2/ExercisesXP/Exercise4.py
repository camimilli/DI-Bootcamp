# Exercise 4: Family And Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age 
        self.last_name = ''

    def is_18(self)->bool:
        '''
        Check if the person is above or below 18 
        '''
        if self.age >= 18:
            return True
        else:
            return False 
        
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        '''
        Creates a new instance from class Person 
        adds the new member to the members list
        '''
        new_member = Person(first_name, age)
        self.members.append(new_member)

    def check_majority(self, first_name)->str:
        '''
        Checks if the member exits in members list
        if yes -> checks if over or under 18 and checks if they can go out with friends
        if not -> returns that person is not part of members list 
        '''
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print('You are over 18, your parents Jane and John accept that you will go out with your friends')
                else:
                    print('Sorry, you are not allowed yo go out with your friends.')
                return 
        
        print(f'Not member with name {first_name} found')
        

    def family_presentation(self)->str:
        '''
        Returns family last name 
        followed by members' first name and age 
        '''
        print(self.last_name)
        for family_member in self.members:
            print(f'{family_member.first_name} {family_member.age}')


millicovsky = Family('Millicovsky')
millicovsky.born('Gisela', 39)
millicovsky.born('Camila', 30)
millicovsky.born('Susana', 74)
millicovsky.born('Leonardo', 80)
millicovsky.born('Alba', 1)
millicovsky.check_majority('Camila')
millicovsky.check_majority('Alba')
millicovsky.check_majority('Mateo')
millicovsky.family_presentation()
