# MRO - Method Resolution Order

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1 

class D(B, C):
    pass 

print(D.num) # 1 
# We get one because MRO checks the closest parent classes (B,C) to check for attributes
# and only then it goes to A 

print(D.mro()) # it will show the MRO of D 
# print(D.__mro__) -> same as .mro()
