import random

user_input = input("Enter a 10 character long word/sentence: ")

if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
elif len(user_input) == 10:
    print("Perfect string")
    print(f"first character: {user_input[0]} \nlast character: {user_input[-1]}")
    sentence_builder = ""
    for letter in user_input:
        sentence_builder += letter 
        print(sentence_builder)
    char_list = list(sentence_builder)
    random.shuffle(char_list)
    shuffled_string = "".join(char_list)
    print(f"Oh no, I left your sentence alone and now a monster made a mess 👹👹👹 -> {shuffled_string}")

    