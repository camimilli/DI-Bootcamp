# # Exercise 1: What's Your Name?

# def get_full_name(first_name, last_name, middle_name=''):
#     if middle_name == '':
#         return f'{first_name.capitalize()} {last_name.capitalize()}'
#     else:
#         return f'{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}'

# print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
# print(get_full_name(first_name="bruce", last_name="lee"))


# Exercise 2: From English To Morse

MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}


REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def english_to_morse(sentence)->str:
    '''
    Converts an English sentence 
    to Morse language 
    '''
    morse = ''
    for letter in sentence:
        if letter == ' ':
            morse += '/'
        else:
            morse += MORSE_CODE_DICT[letter]
            morse += ' '
    return morse 

def morse_to_english(sentence)->str:
    '''
    Converts a Morse sentence
    into English language
    '''
    

print(english_to_morse('HELLO WORLD'))
