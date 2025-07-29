# Daily Challenge: Solve The Matrix

import re 

MATRIX_STR = '7iiTsxh%?i #sM $a #t%'

def string_to_2d(text,n):
    '''
    converts a string into a 2d list 
    based on the text and number of characters to build the list
    '''
    matrix_list = []
    for i in range(0,len(text),n):
        matrix_list.append(text[i:i+n])
    return matrix_list

matrix = string_to_2d(MATRIX_STR, 3)


# Iterate through columns 
def process_columns(matrix):
    second_index = 0
    alpha_only = ''
    char_only = ''
    result = ''


    while second_index != 3:
        for matrix_i in range(len(matrix)):
            current_char = matrix[matrix_i][second_index]
            result += current_char
            if current_char.isalpha():
                alpha_only += current_char
            else:
                char_only += current_char
            
        second_index += 1 

    return alpha_only, char_only, result

    


matrix_alpha_only, matrix_char_only, matrix_with_characters = process_columns(matrix)
# print(f'{matrix_alpha_only}\n{matrix_char_only}\n{matrix_with_characters}')

pattern = r'[^\sa-zA-Z0-9]+'
replacement = ' '


cleaned_sentence = re.sub(pattern, replacement, matrix_with_characters)
print(cleaned_sentence)




# print(temp_string)
# print(alpha_char_index)
# print(non_alpha_char_index)

        


        











def split_string_by_n_chars(text, n):
    return [text[i:i+n] for i in range(0, len(text), n)]

