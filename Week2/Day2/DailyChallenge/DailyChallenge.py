# Daily Challenge: Solve The Matrix


# STEP 1 - TRANSFORM STRING INTO A 2D LIST
MATRIX_STR = '7iiTsxh%?i #sM $a #t%'

def string_to_2d(text,n)->list:
    '''
    converts a string into a 2d list 
    based on the text and number of characters to build the list
    '''
    matrix_list = []
    for i in range(0,len(text),n):
        new_element = text[i:i+n]
        matrix_list.append([letter for letter in new_element])
    return matrix_list

matrix = string_to_2d(MATRIX_STR, 3)

# STEP 2 - PROCESSING COLUMNS 

def process_columns(two_dim_list)->str:
    '''
    Reads a 2D list column by column 
    from top to bottom 
    returns the elements iterated in a string
    '''
    column_counter = 0
    result = ''

    while column_counter != 3:
        for row_index, row in enumerate(two_dim_list):
            for col_index in range(len(row)):
                if col_index == column_counter:
                    result += two_dim_list[row_index][column_counter]                
        column_counter += 1 

    return result

sentence_with_chars = process_columns(matrix)  

# STEP 3 - CLEANING STRING (ALPHA CHARACTERS / REPLACE SYMBOLS WITH SPACES)

def clean_string(text)->str:
    text_to_clean = text
    cleaned_text = ''

    for index, char in enumerate(text_to_clean):
        if char.isalpha():
            cleaned_text += char 
        elif (char.isalpha() == False) and (text_to_clean[index-1].isalpha() == False):
            cleaned_text += ''
        else:
            cleaned_text += ' '
    
    return cleaned_text.strip()

decoded_message = clean_string(sentence_with_chars)
print(decoded_message)