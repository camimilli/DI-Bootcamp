import psycopg2
import requests
import json 
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

connection = psycopg2.connect(
    database = 'countries',
    user = 'camilamillicovsky',
    password = 'Comolashojasdelmar123!',
    host = 'localhost',
    port = '5432'
)

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS countries')

cursor.execute('''CREATE TABLE countries(
               country_id SERIAL PRIMARY KEY,
               country_name VARCHAR (200) NOT NULL,
               capital VARCHAR (200),
               flag_png VARCHAR (200),
               region VARCHAR(200),
               population INTEGER NOT NULL)''')

connection.commit()

print('connection succesfully made. Table was created')

# API REQUEST
response = requests.get('https://www.apicountries.com/countries')
data = response.json()

# adding api request data into json file 
with open(f"{dir_path}\countries.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# getting 4 countries from list of objects 

for i in range(10):
    country_name = data[i]['name']
    # capital = data[i].get('capital') # get is better for api requests as if there's no value it will return 'none' 
    try:
        capital = data[i]['capital']
    except:
        capital = 'Unknown'
    # we do this for countries that have ' as it creates a syntax error
    if '\'' in capital:
        capital = capital.replace('\'', '`')   
    
    # can also do try/except to do:
    # try:
    #   capital = data[i].get('capital')
    # except:
    #   capital = 'Unknown' 
    flag_png = data[i]['flags']['png']
    region = data[i]['region']
    population = data[i]['population']

    cursor.execute(f'''INSERT INTO countries (country_name, capital, flag_png, region, population) 
                   VALUES('{country_name}', '{capital}', '{flag_png}', '{region}', '{population}')''')
    
    connection.commit()


print('table successfully populated')


# Fetch info from database 
cursor.execute("SELECT * FROM countries")

rows = cursor.fetchall()

for row in rows:
    print(row)


# everytime we fetch we need to close the cursor at the end 
cursor.close()
connection.close()