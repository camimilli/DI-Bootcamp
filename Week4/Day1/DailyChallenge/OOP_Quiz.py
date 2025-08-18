import random

# Part 1 : Quizz 

# What is a class? - A blueprint to instantiate objects 
# What is an instance? - An object that belongs to a class with its attributes and methods
# What is encapsulation? - OOP principle where data and methods are bundled together in a class 
# What is abstraction? - OOP principle of hiding information and giving access to it only when needed.
# What is multiple inheritance? - OOP principle that allows new objects to take on the properties of existing objects 
# What is polymorphism? OOP principles that allows object classes to share the same method name while acting differently based on what object calls the methods
# What is a method resolution order or MRO? - the algorithm that tells a class that inherits from other classes from which class to inherit 


# Part 2 : Create a Deck Of Cards Class

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value 

    def __str__(self):
        return f'{self.suit}:{self.value}'
    
class Deck:

    def __init__(self):
        self.deck = []
        available_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        available_values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        for suit in available_suits:
            for value in available_values:
                self.deck.append(Card(suit,value))

    def __str__(self):
        return '\n'.join(str(c) for c in self.deck)

    def shuffle(self):
        return random.shuffle(self.deck)
    
    def deal(self):
        if self.deck == []:
            return "There're no more cards left in this deck"
        dealt_card = random.choice(self.deck)
        self.deck.remove(dealt_card)
        return f'YOUR DEALT CARD: {str(dealt_card)}'
    
    