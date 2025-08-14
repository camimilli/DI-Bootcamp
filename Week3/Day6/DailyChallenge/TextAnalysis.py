# Daily Challenge : Text Analysis

import string, re, translate, os
from collections import Counter

class Text:

# Step 1 
    def __init__(self, text):
        self.text = text 

#Step 2 
    def word_frequency(self, word):
        word_list = self.text.split()
        count = Counter(word_list)
        if word not in count:
            return None
        return True   

# Step 3
    def most_common_word(self):
        word_list = self.text.split()
        frequency_counter = Counter(word_list)
        max_key = max(frequency_counter, key=frequency_counter.get)
        return max_key 

# Step 4 
    def unique_word(self):
        word_list = self.text.split()
        word_list = set(word_list)
        return list(word_list)

# Step 5 
    def from_file(file_path):
        with open(f'{file_path}', 'r', encoding='utf-8') as my_file:
            text = my_file.read()
        return text 

