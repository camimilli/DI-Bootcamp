# MODULES
# name convention: snakecase (lowercase and underscore for whitespaces)
# utility.py module- very common in Python projects, it's like a toolbox where you have functions that you use accross the Python files in your project 

# __pycache__ FOLDER
# File created every time we use modules 
# it caches everything the module has, it's compiled so the interpreter can use the compiled file instead of the module itself makes things faster
# if we change something in the utility module the pycache file will be updated

# IMPORTING FULL MODULE
# import module_name

# IMPORTING A SPECIFIC FUNCTION
# from module_name import function_name

# IMPORTING MORE THAN ONE FUNCTION
# from module_name import function_0, function_1, function_2

# USING ALIAS 
# Assign nickname to each module/function you import
# FOR FUNCTION -> from module_name import function_name as alias_name 
# FOR MODULE -> import module_name as alias_name

# example: from pizza import make_pizza as mp 

# ACCESSING PACKAGES AND MODULES IN A FOLDER
# PACKAGE - folder containing modules 
# SYNTAX TO IMPORT - import package_name.module_name 
# SYNTAX TO USE MODULE - print(package_name.module_name.method_name())






