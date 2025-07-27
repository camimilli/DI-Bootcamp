# Exercise 1: Student Grade Summary

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# calculate average for each student
student_averages = {key:round(sum(value)/len(value)) for (key,value) in student_grades.items()}

def assign_letter_grades(value):
    if value < 60:
        return 'F'
    elif value in range(60,70):
        return 'D'
    elif value in range(70,80):
        return 'C'
    elif value in range (80,90):
        return 'B'
    else:
        return 'A'

# Assign letter grades 
student_letter_grades = {key: assign_letter_grades(value) for(key,value) in student_averages.items()}

# Calculate class average
student_average_list = [value for value in student_averages.values()]
class_average = round(sum(student_average_list)/len(student_average_list))

print(class_average)
print(student_averages)

# Print results 
for key, value in student_letter_grades.items():
    for key in student_averages.keys():
        print(f"{key}:\n- Average grade: {student_averages[key]}\n- Letter grade: {value}") 


# Exercise 2: Advanced Data Manipulation And Analysis

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# Total Sales Calculation
total_sales = {}

for transaction in sales_data:
    product = transaction['product']
    cost = transaction['price']*transaction['quantity']
    if product in total_sales:
        total_sales[product] += cost
    else:
        total_sales[product] = cost

# print(total_sales)
    

# Customer Spending Profile
customer_spending = {}

for transaction in sales_data:
    customer_id = transaction['customer_id']
    amount_spent = transaction['price'] * transaction['quantity']
    if customer_id in customer_spending:
        customer_spending[customer_id] += amount_spent
    else:
        customer_spending[customer_id] = amount_spent

# print(customer_spending)

# Sales Data Enhancement
for transaction in sales_data:
    transaction.update({'total_price':(transaction['price'] * transaction['quantity'])})

# High-Value Transactions
greater_500 = [list for list in sales_data if list['total_price'] > 500]
print(greater_500)
# missing the total price in descending order DO IT AFTER

# Customer Loyalty Identification


# Bonus: Insights and Analysis

