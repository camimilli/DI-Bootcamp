import menu_item as m_i
import menu_manager as m_m 
import psycopg2


def add_item_to_menu():
    '''Ask user for the item name and price 
    they want to add to the database
    and inserts it into the relevant table'''

    while True:
        try:
            user_input = input("\nEnter the item name and price separated by a comma and a space\nExample: Hamburguer, 15: ")
            item_name, item_price = user_input.split(', ')
            item_name = item_name.title()
            item_price = int(item_price)
            break
        except ValueError:
            print("You didn't enter name and price correctly")
            continue 


    try:
        m = m_i.MenuItem(item_name, item_price)
        m.save()
        print('Item was added succesfully')
    except (psycopg2.errors.IntegrityError, psycopg2.errors.ProgrammingError, psycopg2.errors.OperationalError):
        print("We couldn't add your item to the database, contact your database manager for more information or try again later.")
    

def remove_item_from_menu():
    '''
    Asks the user to input the name of the item they want to remove 
    Deletes the item from the relevant table if the item exists
    Prompts the user with an error if the item doesn't exist/if there's an issue deleting the item  
    '''

    user_input = input('\nEnter the name of the item you want to remove: ').title()
    m = m_m.MenuManager()
    item = m.get_by_name(user_input)
    if item:
        try:
            item.delete()
            print('Item deleted successfully')
        except (psycopg2.errors.IntegrityError, psycopg2.errors.ProgrammingError, psycopg2.errors.OperationalError):
            print("We couldn't add your item to the database, contact your database manager for more information or try again later.")
    else:
        print("The item doesn't exist")


def update_item_from_menu():
    '''
    Asks the user to input the name and price of the item they want to update 
    Prompts the user to select which attribute they want to update 
    Executes update method based on their choice if item exists 
    '''

    # Ask user to enter the item they want to update 
    while True:
        try:
            user_input = input("\nEnter the name and price of the item you want to update, separated by a comma and a space.\nExample: Hamburguer, 7: ")
            item_name, item_price = user_input.split(', ')
            item_name = item_name.title()
            item_price = int(item_price)
            break
        except ValueError:
            print("You didn't enter name and price")
            continue 

    # Check if item exists in database 
    mm = m_m.MenuManager()
    item = mm.get_by_name(item_name)

    # If item exists in database create MenuItem object 
    if item:
        m = m_i.MenuItem(item_name, item_price)

        while True:
            try:
                # Ask user which attribute they want to update 
                option_update = input('Choose what you want to update:\n\
- Item Name (N)\n\
- Item Price (P)\n\
- Item Name & Item Price (NP)\n').upper()
                        
                if option_update not in ('N', 'P', 'NP'):
                    raise ValueError('Invalid choice. Please select an option from the menu')
                else:
                    break

            except ValueError as e:
                print(e)
                continue


        # Prompt user to enter new name, price or both based on their choice 

        # Update name only 
        if option_update == 'N':
            name = input("Enter new name: ").title()
            try:
                m.update(new_name = name)
                print('Item price updated successfully')
            except (psycopg2.errors.IntegrityError, psycopg2.errors.ProgrammingError, psycopg2.errors.OperationalError):
                    print("We couldn't add your item to the database, contact your database manager for more information or try again later.")
       
       # Update price only 
        elif option_update == 'P':

            while True:
                try:
                    price = int(input("Enter new price: "))
                    break
                except TypeError:
                    print("Please enter a number")
                    continue
            
            try:
                m.update(new_price=price)
                print('Item price updated successfully')
            except (psycopg2.errors.IntegrityError, psycopg2.errors.ProgrammingError, psycopg2.errors.OperationalError):
                    print("We couldn't add your item to the database, contact your database manager for more information or try again later.")

        elif option_update == 'NP':
            name = input("Enter new name: ").title()

            while True:
                try:
                    price = int(input("Enter new price: "))
                    break
                except TypeError:
                    print("Please enter a number")
                    continue
            
            try:
                m.update(new_name=name, new_price=price)
                print('Item price updated successfully')
            except (psycopg2.errors.IntegrityError, psycopg2.errors.ProgrammingError, psycopg2.errors.OperationalError):
                print("We couldn't add your item to the database, contact your database manager for more information or try again later.")

    else:
        print("The item doesn't exist")


def view_item_from_menu():
    user_input = input('\nEnter the name of the item you want to see: ').title()
    m = m_m.MenuManager()
    item = m.get_by_name(user_input)
    
    if item:
        print(item)
    else:
        print("The item doesn't exist")


def show_restaurant_menu():
    '''Prints all the items from the Menu_Items table
       Returns a message of no items in the menu if table empty'''
    
    mm = m_m.MenuManager()
    restaurant_menu = mm.all_items()
    
    if restaurant_menu == []:
        print("There're no items in the restaurant menu")
    else:
        print('\n*** Restaurant Menu ***')
        for item in restaurant_menu:
            name = item[0]
            price = item[1]
            print('-'*40)
            print(f"Name: {name} || Price: {price}")
        print('\n')

def exit_program():
    '''
    Let's user know they exited the program 
    Calls show_restaurant_menu function 
    Returns False to break out of the main loop 
    '''
    print('\nYou exited the program\n')
    show_restaurant_menu()

    # Returning False so main loop breaks 
    return False 


def show_user_menu():
    ''' 
    Displays program menu to user and executes a specific function 
    based on their choice 
    '''

    while True:

        # Get user input and validate it 
        try:
            user_input = input(f"""\n*** RESTAURANT MANAGEMENT SYSTEM ***
{'-' * 37}                    
- View an Item (V)\n
- Add an Item (A)\n
- Delete an Item (D)\n
- Update an Item (U)\n
- Show the Menu (S)\n
- Exit (X)\n
Select one of the following choices: """).upper()
            
            if user_input not in ('V', 'A', 'D', 'U', 'S', 'X'):
                raise ValueError('Invalid Choice. Please select an option from the menu.')
            elif user_input == 'X':
                break
            else:
                break 
        except ValueError as e:
            print(e)
            continue 

    # add appropiate functions after they're done 
    if user_input == 'V':
        return view_item_from_menu()
    elif user_input == 'A':
        return add_item_to_menu()
    elif user_input == 'D':
        return remove_item_from_menu() 
    elif user_input == 'U':
        return update_item_from_menu()
    elif user_input == 'S':
        return show_restaurant_menu() 
    elif user_input == 'X':
        return exit_program() 