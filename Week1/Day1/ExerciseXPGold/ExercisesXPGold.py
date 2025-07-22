# Exercise 1 - Hello World - I Love Python
print((("Hello World \n") * 4) + (("I love python \n") * 4))

# Exercise 2 - What Is The Season?
month = int(input("Enter the month of your choice by selecting a number from 1 to 12: "))
if month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
elif month >= 9 and month <= 11:
    print("Autumn")
elif month == 12 or month >= 1 and month <= 2:
    print("Winter") 
else:
    print("Invalid Month")

