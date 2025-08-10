# APIs 
# Many APIs communicate in JSON format 
# When you use an API make sure you're aware of the amount of free requests before you get charged - use forloop for a few amount of requests before
# and if you pass it for the program to print that you surpassed your amount of requests 

import requests, json, os 
# the requests library is used to make HTTP requests in Python
# if you don't have this installed, go to terminal and try one of these:
# pip3 install requests 
# pip install requests
# py -m pip install requests 

# Request  
# SYNTAX - response = requests.get('URL')
# printing response will tell you if it was sucesfull (200) or something else 

dir_path = os.path.dirname(os.path.realpath(__file__))

response = requests.get('https://api.chucknorris.io/jokes/random')
print(response) # prints response code if it passed or not 
print(response.text) # gives you json with all values sent through API

# Hold the value data 
data = json.loads(response.text) # we converted the API response to JSON string - it converts it to a dictionary 

print(data['value']) # access value key to display only the joke 

# Store joke in a JSON file to keep it 
with open(f'{dir_path}\jokes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, sort_keys=True) # indent and sort_keys are additional values to make the json file look nicer




