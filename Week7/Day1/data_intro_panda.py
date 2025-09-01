import pandas as pd 

# # Series - Kind of a "list"
# data = pd.Series([1, 3, 5, 7, 9])

# data = {
#     'Name': ['John', 'Anna', 'Peter', 'Linda'],
#     'Age': [28, 34, 29, 32],
#     'City': ['New York', 'Paris', 'Berlin', 'London']
# }

# # DataFrame - List of lists (row/columns)
# df = pd.DataFrame(data)

# my_series = pd.Series(['New York', ''])
# my_series.apply(lambda n: n[0])  

# # Creating a condition that will check it on rows from a field 
# condition = df['Age'] > 30

data = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}

df = pd.DataFrame(data)
print(df.head())
print(df.describe()) # returns information about numerical columns 
print(df.info()) # get info about the dataframe 
print(df.sort_values(by='Price'))
print(df.sort_values(by='Copies Sold'))
condition = df['Genre'] == 'Dystopian'
condition2 = df['Price'] > 10
print(df[condition2])
print(df.groupby('Author').sum('Copies Sold')) 
# here on sum('Copies Sold') it shows only one book, so it gives only one number if there were more books 
# it would sum all the copies sold from all the books from an author and group them with the total sum 