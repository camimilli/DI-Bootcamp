# Challenges #2

def stars_shape(shape, rows)->str:
    '''
    prints a pattern based on the shape and rows passed as arguments
    '''

    if shape == 'pyramid':

        for i in range(rows):
            space = rows - i - 1 
            star = 2 * i + 1 
            print(((space * ' ') + (star * '*')))


    elif shape == 'right_aligned_triangle':
        for i in range(rows):
            space = rows - i - 1 
            star = 1 * i + 1 
            print(((space * ' ') + (star * '*')))


    elif shape == 'diamond':
        space = 0
        star = 1 

        for _ in range(rows):
            print(star * '*')
            star += 1 

        star -= 1 

        for _ in enumerate(rows):
            print(((space * ' ') + (star * '*')))
            star -= 1 
            space += 1 

# stars_shape('pyramid', 20)
# stars_shape('diamond', 20)
# stars_shape('right_aligned_triangle', 9)


# # 1 
# space = 2
# star = 1

# for _ in range(3):
#     print(((space * ' ') + (star * '*')))
#     space -= 1 
#     star += 2


# 2 
# space = 4 
# star = 1 

# for _ in range(5):
#     print(((space * ' ') + (star * '*')))
#     space -= 1 
#     star += 1 


# # 3
# space = 0
# star = 1 

# for _ in range(5):
#     print(star * '*')
#     star += 1 

# star -= 1 

# for _ in range(5):
#     print(((space * ' ') + (star * '*')))
#     star -= 1 
#     space += 1 

