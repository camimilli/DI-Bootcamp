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


class TextModification(Text):

    def remove_punctuation(self):
        punctuation_pattern = r'[' + re.escape(string.punctuation) + ']'
        cleaned_text = re.sub(punctuation_pattern, '', self.text)
        return cleaned_text
    
    def remove_stop_words(self):
        stop_words_en = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
    'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
    'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd',
    'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn',
    'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn',
    'weren', 'won', 'wouldn']
        word_list = self.text.split()
        new_list = [word for word in word_list if word.lower() not in stop_words_en]
        text_no_stop_words = ' '.join(new_list)
        return text_no_stop_words

    def remove_special_characters(self): 
        punctuation_pattern = r'[^a-zA-Z0-9\s]'
        cleaned_text = re.sub(punctuation_pattern, '', self.text)
        return cleaned_text

