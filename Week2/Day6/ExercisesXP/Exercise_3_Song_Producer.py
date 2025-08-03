# Exercise 3: Who's the Song Producer?

class Song: 

    def __init__(self, lyrics):
        self.lyrics = lyrics 

    def sing_me_a_song(self):
        for sentence in self.lyrics:
            print(sentence)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
