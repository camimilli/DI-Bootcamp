# Challenge 1: Sorting

def sort()->str:
    '''
    ask user to input a series of words separated by comma
    returns the list of words ordered alphabetically in a string
    '''
    text = input('Write a few words separated by commas and no spaces (e.g: pinneapple,music,reading):\n')
    words = text.split(',')
    words.sort()
    return (', '.join(words))
    

print(sort())


# Challenge 2: Longest Word

def longest_word(sentence)->str:
    '''
    Returns the longest word in a sentence 
    '''
    words = sentence.split(' ')
    return max(words, key=len)
    

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
    