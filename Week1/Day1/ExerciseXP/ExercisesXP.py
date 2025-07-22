# Exercise 1 - Hello World
print("Hello World \n" * 4)

# Exercise 2 - Some Math
print((99**3)*8)

# Exercise 3 - What Is The Output?
False
True
False
False
False

# Exercise 4 - Your Computer Brand
computer_brand = "Mac"
print(f"I have a {computer_brand} computer")

# Exercise 5 - Your Information
name = "Camila"
age = 30
shoe_size = 37
info = f"{name} is a {age} year old woman which an average feet size of {shoe_size}"
print(info)

# Exercise 6 - A & B
a = 10 
b = 5
if a > b:
    print("Hello World")

# Exercise 7 - Odd Or Even
number_input = int(input("Enter a number: "))
if number_input % 2 == 0:
    print("You entered an even number")
else:
    print("You entered an odd number")

# Exercise 8 - What's Your Name?
user_name = (input("What's your name?: ").casefold()).capitalize()
my_name = "Camila"
if user_name == my_name:
    print("Hello twin, we share the same name")
else:
    print("Booo, we don't have the same name :()")

# # Exercise 9 - Tall Enough To Ride A Roller Coaster
user_height = int(input("Enter your height in cm: "))
if user_height > 145:
    print("You're tall enough to ride")
else:
    print("You need to grow some more to ride")


