# Daily Challenge : Web API To DB

import psycopg2
import requests
import json
import os 
import config as c

dir_path = os.path.dirname(os.path.realpath(__file__))

# ESTABLISHING DB CONNECTION

try:
    connection = psycopg2.connect(
        database = c.DATABASE,
        user = c.USER,
        password = c.PASSWORD,
        host = c.HOST,
        port = c.PORT
    )
except Exception as e:
    print(f"Error: {e}")

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS countries')

cursor.execute('''CREATE TABLE countries(
               country_id SERIAL PRIMARY KEY,
               country_name VARCHAR (200) NOT NULL,
               capital VARCHAR (200),
               flag_png VARCHAR (200),
               region VARCHAR (200),
               population INTEGER NOT NULL)''')

connection.commit()
print('connection succesfully made. Table was created')


# API REQUEST - CREATING JSON
url_countries_api = 'https://restcountries.com/v3.1/all?fields=name,capital,flag,population,region'
response = requests.get(url_countries_api) 
data = response.json()

with open(f"{dir_path}/countries.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)


# EXTRACTING VALUES FROM JSON
# UPLOADING TO DB

for i in range(10):
    country_name = data[i]['name']['common']
    try:
        capital = data[i]['capital'][0]
    except:
        capital = 'Unknown'
    flag = data[i]['flag']
    region = data[i]['region']
    population = data[i]['population']

    cursor.execute(f'''INSERT INTO countries (country_name, capital, flag_png, region, population)
                   VALUES('{country_name}', '{capital}', '{flag}', '{region}', '{population}')''')
    
    connection.commit()

print('Values inserted successfully')


cursor.close()
connection.close()

