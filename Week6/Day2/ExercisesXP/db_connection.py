import psycopg2

connection = psycopg2.connect (
    database = 'restaurant',
    user = 'camilamillicovsky',
    password = 'Comolashojasdelmar123!',
    host = 'localhost',
    port = '5432'
)

cursor = connection.cursor()