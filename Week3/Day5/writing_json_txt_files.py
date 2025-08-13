# Python writing files (.txt, .json, .csv)
# w - write (or overwrites a file)
# x - writes if the file doesn't already exist 
# a - append new data on existing file 

############################

# Example 'a', 'w', string 

txt_data = 'I like pizza!'

absolute path 
file_path = 'output.txt'

try:
    with open(file_path, 'a') as file:
        file.write("\n" + txt_data) 
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("This file already exists!")

############################
# Working with collections 

employees = ['Eugene', 'Squidward', 'Spongebob', 'Patrick']

file_path = 'output.txt'

try:
    with open(file_path, 'a') as file:
        for employee in employees:
            file.write('\n' + employee)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("This file already exists!")

############################
# .json 
# dictionaries are great candidates to be converted to json 

import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook",  
}

file_path = 'output.json'

try:
    with open(file_path, 'w') as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("This file already exists!")

############################
# .csv 

import csv 

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = 'output.csv'

try:
    with open(file_path, 'w', newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path} was created")
        
except FileExistsError:
    print("This file already exists!")