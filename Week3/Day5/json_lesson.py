import json 
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

# CONVERT A DICT TO JSON FILE 
my_family = {
    'parents': ['Beth', 'Jerry'],
    'children': ['Summer', 'Morty']
}

# we use 'w' because we're creating a file 
# we don't need encoding because is not text, it's json 
# with open(f'{dir_path}/family.json', 'w') as f:
#     # first arg: the dictionary we want to convert / second arg: to where we want to dump the dict to (f)
#     json.dump(my_family, f) 


# CONVERT A DICT TO JSON STRING 
# we only pass 1 arg -> what we want to make into a json string
json_my_family_string = json.dumps(my_family)
# print(type(json_my_family_string)) # when converting it's considered a string because is json string, when we print it looks like dict 


# CONVERT FROM JSON FILE TO DICTIONARY
with open(f'{dir_path}/family.json', 'r') as f:
    # pass the object you created into arg (f)
    my_family2 = json.load(f)

print(my_family2)


# CONVERT FROM JSON STRING TO DICTIONARY
parsed_family = json.loads(json_my_family_string)
print(type(parsed_family)) # it's dict because we parsed it 



