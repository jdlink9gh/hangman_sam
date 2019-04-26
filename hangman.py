import urllib.request
import shutil
import random
import pathlib

class Hangman():
    def __init__(self):
        self.wordLength = 12    # minimum length of word chosen by game
        self.word = str()       # word chosen by game
        self.gamestate = 0      # whether game is in progress or not
        self.stateHM = 0        # state of the hangman; 1-6
        self.guess = str()      # input from player; 1 alphabetical character
        self.lines = list()     # list of words read from text file

    def openFile(self):
        # This method does multiple things. First, it checks if the ./word_data/ directory exists and creates it if it
        # does not exist. Second, it checks if the word.txt file exists in the directory and downloads it if it does
        # not exist. Third, it opens the file and writes the contents to a list.

        # checking and creating the directory if necessary
        pathlib.Path('./word_data/').mkdir(parents=True, exist_ok=True)

        # storing the relative file path to the words.txt file
        filePath = './word_data/words.txt'

        try:
            # checking if the file exists
            with open(filePath) as f:
                print('file exists')
        except FileNotFoundError:
            # downloading the file to the directory if it does not exist
            print('file does not exist')
            url = 'http://norvig.com/ngrams/sowpods.txt'
            urllib.request.urlretrieve(url, filePath)
            print('file downloaded to ' + filePath)
        finally:
            # storing the file contents as a list
            with open(filePath) as f:
                self.lines = f.readlines()
            print('file read')

    def wordPick(self):
        # This method randomly selects a word of a minimum length from the stored list
        while len(self.word) < self.wordLength:
            self.word = random.choice(self.lines)

        print(self.word)

    def 

    def printhangman(self, wrongGuesses):
        # This method prints on of the 7 states of the hangman
        if wrongGuesses == 0:
            print('|‾‾‾‾‾‾‾|')
            print('|')
            print('|')
            print('|')
            print('|')
        elif wrongGuesses == 1:
            print('|‾‾‾‾‾‾‾|')
            print('|     O')
            print('|')
            print('|')
            print('|')
        elif wrongGuesses == 2:
            print('|‾‾‾‾‾‾‾|')
            print('|     O')
            print('|     |')
            print('|     ')
            print('|')
        elif wrongGuesses == 3:
            print('|‾‾‾‾‾‾‾|')
            print('|     O')
            print('|    /|')
            print('|     ')
            print('|')
        elif wrongGuesses == 4:
            print('|‾‾‾‾‾‾‾|')
            print('|     O')
            print('|    /|\\')
            print('|     ')
            print('|')
        elif wrongGuesses == 5:
            print('|‾‾‾‾‾‾‾|')
            print('|     O')
            print('|    /|\\')
            print('|    /')
            print('|')
        elif wrongGuesses == 6:
            print('|‾‾‾‾‾‾‾|')
            print('|     O')
            print('|    /|\\')
            print('|    / \\')
            print('|')


game = Hangman()
