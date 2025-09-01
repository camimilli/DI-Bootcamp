import menu_editor as m_e
import db_connection as db 


# Activates the restaurant management system 

active_program = True

while active_program:

    # Display options menu 
    program = m_e.show_user_menu()
    if program == False:
        active_program = False 

        # Close connection to db
        db.cursor.close()
        db.connection.close()

        # Break out of the program 
        break 
    else:
        continue




