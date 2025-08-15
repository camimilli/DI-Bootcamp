from anagram_checker import AnagramChecker
import string, re 

pattern_alphabet = r'^[a-zA-Z]+$'

# game_on = True 

# while game_on == True:


while True:
    try:
        user_input = input("Please enter *one* word - type 'q' to exit:  ")

        if " " in user_input:
            print('Your input has more than one word, we only allow one')
            continue

        if re.match(pattern_alphabet, user_input) == None:
            print('you can only write words with alphabetic characters (a-z)')
            continue

        elif user_input == 'q':
            break

        else:
            user_input = user_input.strip().lower()
            print(f'YOUR WORD: "{user_input.upper()}"')
            anagram_checker = AnagramChecker()

            if anagram_checker.is_valid_word(user_input):
                print('this is a valid English word')
                anagrams = anagram_checker.get_anagrams(user_input)
                if anagrams == []:
                    print("there're no anagrams for your word 😭")
                else:
                    formatted_anagrams = ', '.join(anagrams)
                    print(f"Anagrams for your word: {formatted_anagrams}")
                    continue 
            else:
                print('The word you enter is not a valid English word.')
                continue

    except Exception as e:
        print(f'{e}')


