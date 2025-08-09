# Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        '''
        returns the amount of money and its currency
        '''
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
        else:
            return f'{self.amount} {self.currency}'
        
    def __int__(self):
        '''
        converts string into an int 
        '''
        return int(self.amount)
    
    def __repr__(self):
        '''
        returns the amount and the currency 
        '''
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
        else:
            return f'{self.amount} {self.currency}'
    
    def __add__(self, other):
        return int(self.amount) + int(other)

# check the ifistance and how to apply it here 
    def __iadd__(self,other):
        self += other
        return self  
    
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
c1 += 5
print(c1)
c1 += c2
print(c1)