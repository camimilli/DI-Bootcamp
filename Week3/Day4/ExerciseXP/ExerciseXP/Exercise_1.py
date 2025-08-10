# Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount 

    def __str__(self):
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
    
        return f'{self.amount} {self.currency}' 
    
    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
    
        return f'{self.amount} {self.currency}' 

    def __add__(self, other):
        if isinstance(other, (int, float)) and other > 0:
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise ValueError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError('Unsupported type for addition.')

    def __iadd__(self, other):
        if isinstance(other, (int, float)) and other > 0:
            self.amount += other 
            return self 
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise ValueError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            self.amount += other.amount
            return self
        else:
            return TypeError('Unsupported type for addition.')
        
    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)

print(int(c1))

print(repr(c1))

print(c1 + 5)

print(c1 + c2)

print(c1)

try:
    c1 += 5
    print(c1) 
except Exception as e:
    print(f'{e}')

try:
    c1 += c2
    print(c1) 
except Exception as e:
    print(f'{e}')

try:
    print(c1 + c3)
except Exception as e:
    print(f'{e}')

