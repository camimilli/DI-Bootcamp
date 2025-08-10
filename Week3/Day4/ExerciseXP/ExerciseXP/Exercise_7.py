# Exercise 7: Faker Module

from faker import Faker 

fake = Faker()

users = []

def add_users(num_users):
    for _ in range(num_users):
        user = {}
        user['name'] = fake.name()
        user['address'] = fake.address()
        user['language_code'] = fake.language_code()
        users.append(user)

add_users(3)
print(users)

