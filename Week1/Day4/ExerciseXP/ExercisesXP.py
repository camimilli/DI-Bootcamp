# Exercise 1: Favorite Numbers
my_fav_numbers = {1,3,9,5}
numbers_to_add = {15,25}
my_fav_numbers.update(numbers_to_add)
my_fav_numbers.remove(25)
friends_fav_numbers = {2,4,8,10,5}
our_fav_numbers = my_fav_numbers.union(friends_fav_numbers)
print(our_fav_numbers)


# Exercise 2: Tuple
# numbers = (1, 5, 20, 30)
# numbers.append(4)
# can't add more elements as sets are immutable


# Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0,'Apples')
print(basket.count('Apples'))
basket.clear()
print(basket)


# Exercise 4: Floats
# A float is a number with a decimal and an integer is a whole number
float_numbers = []

for num in range(2,6):
    float_numbers.append(num-0.5)
    float_numbers.append(num)

print(float_numbers)


# Exercise 5: For Loop

# print numbers 1-20 
for number in range(1,21):
    print(number)

# print even numbers between 1-20
for i, number in enumerate(range(1,21)):
    if i % 2 == 0:
        print(number)


# Exercise 6: While Loop

user_name = input("Enter your name: ")

while not user_name.capitalize() == "Camila":
    user_name = input("Enter your name: ")


# Exercise 7: Favorite Fruits

# Ask input and create fruits list 
fruits = input("Type your favorite fruits separated by spaces: ")
fruits_list = fruits.split(" ")

# Ask user to input fruit 
fruit = input("Type the name of any fruit: ")
if fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy")
else:
    print("You chose a new fruit. I hope you enjoy it!")


# Exercise 8: Pizza Toppings
pizza_toppings = []
topping_input = input("Write which topping you want to add to your pizza (type 'quit' to finish): ")
topping_counter = 0

while not topping_input == "quit":
    print(f"Adding {topping_input} to your pizza.")
    topping_input = input("Add another topping (type 'quit' to finish): ")
    topping_counter += 1 
    pizza_toppings.append(topping_input)

# Unpacking topping into string 
pizza_toppings.remove("quit")
pizza_toppings_comma = ", ".join(pizza_toppings)

# Returns toppings' list, price and total price of order 
topping_total = topping_counter * 2.50
print(f"Toppings you chose: {pizza_toppings_comma}\nBase price: $10\nToppings total for {topping_counter} toppings: ${topping_total}\nPizza total: ${topping_total+10}")


# Exercise 9: Cinemax Tickets 

total_cost = 0

while True:
    user_age = int(input("Enter your age (type 0 to quit): "))
    if user_age == 0:
        break
    elif user_age < 3:
        total_cost += 0
    elif 3 <= user_age <= 12:
        total_cost += 10
    else:
        total_cost += 15 

print(f"The total cost for your tickets is: ${total_cost}")

# BONUS EXERCISE 9 - Program - group of teenagers 

attendees_ages = []

while True:
    user_age = int(input("Enter your age (type 0 to quit): "))
    if user_age == 0:
        break
    elif 21 >= user_age >= 16:
        attendees_ages.append(user_age)

print(attendees_ages)


# # Exercise 10: Sandwich Orders - ***NEED TO FINISH***
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

# Remove pastrami orders 
for orders in range(len(sandwich_orders)):
    if "Pastrami" in sandwich_orders:
        sandwich_orders.remove("Pastrami")

# Prepare sandwiches, pass to finish list
counter = 0
finished_sandwiches = []

while counter != len(sandwich_orders):
    for sandwich_order in sandwich_orders:
        print(f"I made your {sandwich_order} sandwich.")
        finished_sandwiches.append(sandwich_order)
        counter += 1 
        
print(finished_sandwiches)    