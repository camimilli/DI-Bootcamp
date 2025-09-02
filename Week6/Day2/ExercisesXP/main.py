import menu_editor as m_e
import db_connection as db 


# Activates the restaurant management system 

active_program = True

while active_program:

    # Display options menu 
    restaurant_manager_system = m_e.show_user_menu()
    if restaurant_manager_system == False:
        active_program = False 
        break 
    else:
        continue




