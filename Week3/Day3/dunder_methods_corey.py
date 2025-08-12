# Dunder Methods
# Allow us to emulate built-in behavior in Python 
# Apply operator overloading 
# always add at least repr method, although always good to have both because if you don't have str and you call str on an object the fallback is repr 

class Employee: 

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
        self.pay = int(self.pay * self.raise_amount)

    # used for debugging, meant for devs
    def __repr__(self)->str:
        '''
        Returns a str in a format that allows
        to recreate an object 
        '''
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # used as a display to the end user 
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email) 

    def __add__(self, other)->int:
        '''
        returns combined salary of two employees 
        '''
        return self.pay + other.pay 

    def __len__(self)->int:
        '''
        returns the length of the employee's fullname
        '''
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# __STR__ and __REPR__ 
print(emp_1) # uses __str__ 
print(repr(emp_1)) # uses __repr__
print(emp_1.__str__()) # same as doing print(emp_1) or print(str(emp_1)

# __ADD__ 
print(emp_1 + emp_2) 

# __LEN__
print(len(emp_1))


# EXAMPLE 2 

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        # allows you to define how your object is represented as a string 
        return f'{self.color}'

    def __len__(self):
        return 5 

    def __del__(self):
        print('deleted!') 

    # allows to call methods through objects 
    def __call__(self):
        return('yess??')
    
    def __getitem__(self, i):
        # enables objects to support indexing or key-based access using square braket notation
        return self.my_dict[i]


action_figure = Toy('red', 0) 
print(action_figure) # red 
print(len(action_figure)) # 5 
# del action_figure # del allows you to delete an object, instance/class attribute and prints what's in __del__ 
print(action_figure()) # using the __call__ method 
print(action_figure['name'])