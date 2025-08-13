# Exercise 1: Random Sentence Generator

import os 
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = f'{dir_path}/words.txt'

# Step 1 
def get_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words_list= f.read().splitlines()
    return words_list

# Step 2
def get_random_sentence(sentence_length):
    list_words = get_words_from_file(file_path)
    new_sentence = []
    for _ in range(sentence_length):
        new_sentence.append(random.choice(list_words))
    new_sentence = ' '.join(new_sentence)
    return new_sentence.lower()
        
# Step 3 

def main():
    # welcome user to program
    print('Welcome to the random sentence maker')
    while True:
        try:
            sentence_length = int(input('Enter the number of words you want in your sentence, you can pick between **2-20**:\n'))
            if sentence_length in range(2,21):
                random_sentence = get_random_sentence(sentence_length)
                print(random_sentence)
                break
            else:
                print('You needed to enter a number between 2 and 20.\n')
                break
        except ValueError:
            # Catches if input is not integer 
            print('Invalid input. You needed to enter a number between 2, and 20.')
            break 
        except Exception as e:
            # generic catch-all for other unexpected errors 
            print(f'{e}')
            print('The program ended')
            break


main()