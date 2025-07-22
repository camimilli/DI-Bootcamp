# Exercise 1 : Use The Terminal
""" When we type python3 in the terminal, the system executes the Python program without us needing to specify its full location
 — because the directory containing python3 is included in our PATH folder. """

# Exercise 2 - Alias
# alias py = 'python3' 

# Exercise 3 - Outputs
True
True
False
False
True
False
True
False
5
10

# Exercise 4 - How Many Characters In A Sentence?
my_text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit," 
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." 
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco" 
    "laboris nisi ut aliquip ex ea commodo consequat." 
    "Duis aute irure dolor in reprehenderit in voluptate velit" 
    "esse cillum dolore eu fugiat nulla pariatur." 
    "Excepteur sint occaecat cupidatat non proident," 
    "sunt in culpa qui officia deserunt mollit anim id est laborum.")

print(len(my_text))

# Exercise 5 - Longest Word Without A Specific Character
 
longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence you can without the character 'A': ")
    if "A" in sentence.upper():
       print("Your sentence has an 'A', please try again")
       continue
    if len(sentence) > len(longest_sentence):
        print("Congratulations!")
        longest_sentence = sentence 
    

    