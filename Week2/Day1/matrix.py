# MATRIX - 2D lists 
# Used to create grid like structures inside of Python 
# Important as come up a lot in machine larning/image processing 

# matrix with 4 rows and 3 columns
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

########################################

# ACCESSING MATRIX

# Access row 1, column 2 
# first index = row 
# second index = column

print(matrix[0][1]) 

########################################

# 2D LISTS & NESTED LOOPS

for row in matrix:
    for col in row:
        print(col)

