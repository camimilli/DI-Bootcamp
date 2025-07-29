# Timed Challenge 1 

def count_character(sentence, char):
    counter = 0
    for letter in sentence:
        if char == letter:
            counter +=1 
    return counter

print(count_character('This is a great example', 'y'))