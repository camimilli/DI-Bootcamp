# PYTHON FILE I/O 
# this module is useful when we work with files/folders it helps us to navigate our OS (operational system)
# Python file operations: opening a file, reading from it, writing into it, closing it 

import os 

# There's old version Python to manipulate files, now there's a new way
# Old version problem -> people forgot to close the file f.close()
# New version doesn't need f.close() we use with open... 

# ########################################

# # HOW TO READ A FILE - NEW WAY 

# # first arg -> text file / sec arg-> mode (read, write, append...) / third arg (optional) -> encoding='utf-8' (for english)

# # variable that leads to the folder where the file I'm working on is located 
dir_path = os.path.dirname(os.path.realpath(__file__))
# # print('dir path: ', dir_path)

# # mac uses / for the path and windows \ 
# # we apply the variable {dir_path} before the name of the file to get the file's path  
# # with open(f'{dir_path}/secrets.txt', 'r', encoding='utf-8') as file_obj:
# #     file_content = file_obj.read() # we apply the method on the obj (file_obj in our case)

# #     print(file_content)

# ########################################

# # COMMON METHODS

# # STAR WARS EXERCISE
# # Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following steps

# # Read the file line by line

with open(f'{dir_path}/star_wars.txt', 'r', encoding='utf-8') as f:
    txt_list = f.readlines() # readlines() returns a list 

    for line in txt_list:
        print(line)
    print('end of document') # good to make sure that it printed everything


# Read only the 5th line of the file
    print(txt_list[4]) 



# Read only the 5 first characters of the file
    print(txt_list[0][:4])



# Read all the file and return it as a list of strings. Then split each word into letters
# using list comprehension
# list(word) separates de letters of a word into its characters 
temp_letters = [list(line) for line in txt_list]
print(temp_letters)


# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file

# Solution using dictionary
counts = {'Darth': 0, 'Luke': 0, 'Lea': 0}

for line in txt_list:
    line = line.strip() # to remove the \n from the list
    if line == 'Darth':
        counts['Darth'] += 1 
    elif line == 'Luke':
        counts['Luke'] += 1 
    elif line == 'Lea':
        counts['Lea'] += 1  

print(counts)

# solution using count in list 
txt_list_strip = [line.strip() for line in txt_list] 
Darth = txt_list_strip.count('Darth')
Luke = txt_list_strip.count('Luke')
Lea = txt_list_strip.count('Lea')

print(Darth)
print(Luke)
print(Lea)



# Append your first name at the end of the file
with open(f'{dir_path}/star_wars.txt', 'a', encoding='utf-8') as f:
    # f.seek(0) # the cursor goes to the beginning of the file 
    f.seek(0, os.SEEK_END) # the cursor is at the end of the file 
    f.write('\nCamila') # appends the string to the file
    print('succesfully added') # to know the program works as expected


# Append "SkyWalker" next to each first name "Luke"
# If we want to modify text that's already on the file, we can't do a for loop, check where the 'Luke' word is and change the text 
# using index like we normally do it because the object we're opening can't be directly changed
# we need to put the changes in a temp list and then overwrite the document with the list
# we can add new text at beginning/end 
# the solution to do it: 

# THIS DOESN'T WORK! TRYING TO MODIFY OBJECT
for i, name in enumerate(txt_list):
    if name.strip() == 'Luke':
        txt_list[i] = f'{name} Skywalker'
print('succesfuly changed')

# THE RIGHT SOLUTION

# create temp list copying the list might not be the best solution
# because it creates anothe for loop 
temp_list = txt_list 

for i, name in enumerate(temp_list):
    if name.strip() == 'Luke':
        temp_list[i] = f'{name} Skywalker'
print('succesfuly changed')


# might be better in terms of performance:
modified_lines = []
for line in txt_list:
    if line.strip() == 'Luke':
        modified_lines.append('Luke Skywalker\n')
    else:
        modified_lines.append(line)

# open file with mode "write"
with open(f'{dir_path}/star_wars.txt', 'w', encoding='utf-8') as f:
    f.seek(0) # when we overwrite we need to make sure that seek is at 0 (beginning of file)
    f.writelines(modified_lines) # we overwrite 
