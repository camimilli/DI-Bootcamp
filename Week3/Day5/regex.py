# Regular Expressions RegEX - Sequence of characters that forms a search pattern
# Used to search for and replace specific patterns 


import re 

# re.findall - returns a list of strings containing all matches of the specified pattern
string = 'at what time?'
match = re.findall('at', string)
print(match) # ['at', 'at']


# re.search - returns a match object in case a match is found - if more than 1 occurrence, only first match returned, no ocurrence found returns None

string = 'This is where it all begins'
match = re.search('begins', string)
if (match):
    print("String found at:",match.start())
else:
    print("String not found!")


# re.split() 
# splits the string into a list of substrings based on a pattern. if you want to use 'a'
# the string will be splitted everytime an 'a' appears but won't be included in the list itself
# in case there's no match the string will be returned as it is, in a list

string = 'at what time?'
match = re.split('a', string)
print(match) # ['', 't wh', 't time?']


# re.sub()
# replaces ocurrences of a particular sub-string with another sub-string
# syntax: the sub-string to replace, the sub-string to replace with, the actual string
# \s is a special sequence that matches any single whitespace character (space, tab, newline, carriage return, form feed, vertical tab, etc)

string = 'at what time?'
match = re.sub("\s", "!!!", string)
print(match) # at!!!what!!!time?


