# @classmethod 
# Takes the class as the first argument instead of self
# USAGE:
# provide multiple ways to create our objects (alternative constructor)


# @staticmethod 
# Behave like regular functions (don't need self/cls as args) but still belong to the class 
# To know if your method should be static -> if you don't access the instance of the class anywhere within the function, make it static

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount 

    # alternative constructor using @classmethod - use 'from' prefix convention
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # this line creates a new employee 
        
    @staticmethod
    def is_workday(day):
        '''
        Takes a day and returns the workday
        is in the class because it has logical connection to the employee class
        but doesn't depend on any specific instance/class method/attribute
        '''
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# using from_string method to create a new object (alternative method)
emp_str_1 = 'John-Doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())

# using set_raise_amt() 
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# using is_workday() staticmethod 
import datetime
my_date = datetime.date(2025, 8, 10) # Sunday
print(Employee.is_workday(my_date)) # False 

##############################



