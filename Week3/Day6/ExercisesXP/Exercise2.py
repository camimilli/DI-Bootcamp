# Exercise 2: Working with JSON 

import json, os

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load the JSON string
parsed_sampleJson = json.loads(sampleJson)

# Step 2: Access the nested "salary" key
print(parsed_sampleJson['company']['employee']['payable']['salary'])

# Step 3: Add the "birth_date" key
parsed_sampleJson['company']['employee']['birth_date'] = '1994-10-08'

# Step 4: Save the JSON to a file 
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = f'{dir_path}/sampleJson.json'

with open(file_path, 'w') as f:
    json.dump(parsed_sampleJson, f, indent=4)
    print("Json file 'sampleJson.json' has been created")

