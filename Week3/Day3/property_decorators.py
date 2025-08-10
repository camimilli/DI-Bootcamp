# @property decorator
# it allows us to define an attribute in a method but we can access it as attribute
# Allows us to give our class attributes getter, setter and deleter functionality
# http://youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last 
        # not in use anymore because of def email() self.email = first + '.' + last + '@email.com'

    @property 
    # if it didn't have property on top, we'd need to call it as a method 
    # and it wouldn't be considered an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # setter
    @fullname.setter 
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first 
        self.last = last 

    # deleter
    @fullname.deleter  
    def fullname(self):
        print('Delete Name!')
        self.first = None 
        self.last = None 
    

emp_1 = Employee('John', 'Smith')

# using setter to change first, last name and email 
emp_1.fullname = 'Corey Shafer' 

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# using deleter 
del emp_1.fullname 