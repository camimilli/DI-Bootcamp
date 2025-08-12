from math import pi 
from functools import total_ordering 

@total_ordering # implement so I don't need to define __lt__
class Circle:

    circles = []

    def __init__(self, radius):
        self.radius = radius
    # check how to make sure that the user can 
        Circle.circles.append(self)

    @property 
    def area(self)->int:
        '''
        Calculates the area of a circle 
        '''
        return pi * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        '''
        Alternative constructor with diameter 
        calculates radius using diameter / 2 
        '''
        radius = diameter / 2 
        return cls(radius) 
        
    
    def __str__(self):
        return f'This circle has a radius of {self.radius}'
    
    def __add__(self, other):
        '''
        Adds the radius of two circles and returns
        a new object with the calculated radius 
        '''
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise ValueError('The argument you passed as "other" is not from the Circle class')
        
    def __gt__(self, other)->bool:
        '''
        Checks is the radius of an object of the class 
        is greater than the other object's radius 
        '''
        if isinstance(other, Circle):
            if self.radius > other.radius:
                return True 
            else:
                return False
        else:
            raise ValueError('The argument you passed as "other" is not from the Circle class')
        

    def __eq__(self, other)->bool:
        '''
        Checks is the radius of an object of the class 
        is equal to other object's radius 
        '''
        if isinstance(other, Circle):
            if self.radius == other.radius:
                return True
            else:
                return False
        else:
            return ValueError('The argument you passed as "other" is not from the Circle class')


Circle1 = Circle(5)
Circle2 = Circle(10)

# check adding circle and int - shouldn't work 
try:
    Circle3 = Circle1 + 2 
except Exception as e:
    print(f'{e}')

try:
    Circle3 = Circle1 + Circle2 
except Exception as e:
    print(f'{e}')

# checking __str__ works and displays attributes 
print(Circle3)

# compare which circle is bigger 
try:
    print(Circle3 > Circle1)
except Exception as e:
    print(f'{e}')

# check if two circles are equal 

try:
    print(Circle1 == Circle1)
except Exception as e:
    print(f'{e}')

# check @classmethod diameter
circle_with_diameter = Circle.from_diameter(7)
print(Circle.circles)

# sorted()
circle_list = [Circle1, Circle2, Circle3, circle_with_diameter]
ordered_list = sorted(circle_list)

for circle in ordered_list:
    print(circle.radius)