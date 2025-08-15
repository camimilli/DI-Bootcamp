# Mini Project : Anagram Checker 

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = f'{dir_path}/sowpods.txt'

class AnagramChecker: 

    def __init__(self):
        with open(f'{file_path}', 'r', encoding='utf-8') as f:
            self.word_list = f.read().splitlines()

    def is_valid_word(self, word)->bool:
        '''
        Checks user input is a word in the words_list 
        '''
        return word.upper() in self.word_list

    @classmethod
    def is_anagram(cls, word1, word2)->bool:
        '''
        Compares two words, returns True if they contain the same letters
        '''
        return sorted(word1) == sorted(word2) 


    def get_anagrams(self, word)->list:
        '''
        Finds all anagrams for word 
        Returns a list with the anagrams
        '''
        anagrams = []
        
        for word_in_list in self.word_list:
            word_in_list = word_in_list.lower()
            if word_in_list != word:
                if AnagramChecker.is_anagram(word, word_in_list):
                    anagrams.append(word_in_list)
        
        return anagrams



