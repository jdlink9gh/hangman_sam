import urllib.request
import shutil
import random

class Hangman():
    def __init__(self):
        self.wordLength = 12     # minimum length of word chosen by game
        self.word = str()       # word chosen by game
        self.gamestate = 0      # whether game is in progress or not
        self.stateHM = 0        # state of the hangman; 1-6
        self.guess = str()

    def wordPick(self):

        fileName = 'sowpods.txt'

        try:
            data = open(fileName)
        except FileNotFoundError:
            url = 'http://norvig.com/ngrams/sowpods.txt'
            with urllib.request.urlopen(url) as response, open(fileName, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
        finally:
            with open(fileName) as f:
                lines = f.readlines()

                while len(self.word) < self.wordLength:
                    self.word = random.choice(lines)




game = Hangman()
game.wordPick()