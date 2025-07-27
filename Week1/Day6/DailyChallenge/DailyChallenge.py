# Challenge 1: Letter Index Dictionary

letters = {}

word = input("Enter a word: ")
    
for index, char in enumerate(word):
    if char in letters:
        letters[char].append(index)
    else:
        letters.update({char:[index]})

print(letters)


# Challenge 2: Affordable Items

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# takes '$X' returns X 
def dollar_to_int(price):
    if ',' in price:
        price = price.replace(',','')
    price = int(price.replace('$',''))
    return price

# convert values from $ to int 
wallet = dollar_to_int(wallet)

for key,value in items_purchase.items():
    items_purchase[key] = dollar_to_int(value)

# Calculate and return affordable items  
affordable_items = []

for item in items_purchase.keys():
    if items_purchase[item] < wallet:
        affordable_items.append(item)

# sort list alphabetically        
affordable_items = sorted(affordable_items)

if affordable_items == []:
    print('Nothing')
else:
    print(affordable_items)




