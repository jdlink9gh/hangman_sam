import urllib.request
import copy
import random
import pathlib
import time
import argparse
import string

class Hangman():

    def __init__(self, length):
        self.stateHM = 0        # state of the hangman; 1-6
        self.guess = str()      # input from player; 1 alphabetical character
        self.lines = list()     # list of words read from text file
        self.word = str()       # word chosen by the program
        self.minlength = length    # minimum length of the word chosen by the program

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
        # self.minlength = int(args.minlength)
        self.word = str()  # word chosen by game

        # selecting a random word from the list that has a length greater than the specified minimum
        while len(self.word) < self.minlength:
            self.word = random.choice(self.lines).lower()
            self.word = self.word[:-1]

        # print(self.word + '\n')

    def printhangman(self, wrongGuesses):
        # This method prints on of the 7 states of the hangman
        if wrongGuesses == 0:
            print('  |‾‾‾‾‾‾‾|')
            print('  |')
            print('  |')
            print('  |')
            print('__|__\n')
        elif wrongGuesses == 1:
            print('  |‾‾‾‾‾‾‾|')
            print('  |     O')
            print('  |')
            print('  |')
            print('__|__\n')
        elif wrongGuesses == 2:
            print('  |‾‾‾‾‾‾‾|')
            print('  |     O')
            print('  |     |')
            print('  |     ')
            print('__|__\n')
        elif wrongGuesses == 3:
            print('  |‾‾‾‾‾‾‾|')
            print('  |     O')
            print('  |     |')
            print('  |    /')
            print('__|__\n')
        elif wrongGuesses == 4:
            print('  |‾‾‾‾‾‾‾|')
            print('  |     O')
            print('  |     |')
            print('  |    / \\')
            print('__|__\n')
        elif wrongGuesses == 5:
            print('  |‾‾‾‾‾‾‾|')
            print('  |     O')
            print('  |    /|')
            print('  |    / \\')
            print('__|__\n')
        elif wrongGuesses == 6:
            print('  |‾‾‾‾‾‾‾|')
            print('  |     O')
            print('  |    /|\\')
            print('  |    / \\')
            print('__|__\n')

    def newGame(self):

        self.openFile()
        self.wordPick()

        letters = list(string.ascii_lowercase)
        guessed = copy.deepcopy(letters)
        guesses = ''
        target = ''
        output = ''
        stateHM = 0

        for char in self.word:
            target += ' ' + char + ' '

        for char in self.word:
            output += ' _ '
        print(output)

        while stateHM < 6:
            output = ''

            print(*guessed, sep=' ')
            guess = input("Choose a letter: ")
            guess = guess.lower()

            if guess in letters:
                if guess in guessed:
                    guessed.remove(guess)

                if guess not in guesses:
                    guesses += guess

                    if guess not in self.word:
                        print(f'{guess} is not in the word!')
                        stateHM += 1
                    else:
                        print(f'{guess} is in the word!')

                else:
                    print(f'You already guessed "{guess}"!')

                time.sleep(1)
                self.printhangman(stateHM)

                for char in self.word:
                    if char in guesses:
                        output += ' ' + char + ' '
                    else:
                        output += ' _ '

                print(output)

                if output == target:
                    print(f'You won in {len(guesses)} guesses!')
                    break
                elif stateHM == 6:
                    print(f'You lose!\nThe word was {self.word}')
                    break
            elif len(guess) != 1:
                print("Please pick one letter from the list...")
            else:
                print(f'"{guess}" is not a letter! Try again...')

            time.sleep(.75)


        again = input('Play again? (y/n)')
        if again == 'y':
            self.newGame()
        else:
            print("Thanks for playing!")

def main():
    # driver function if hangman.py is run

    # the next 3 lines of code setup the CLI input using the argparse library
    parser = argparse.ArgumentParser(description='Play a game of Hangman')
    parser.add_argument('-l', '--minlength', type=int, metavar='', required=True,
                        help='Minimum length of the word you would like to guess')
    args = parser.parse_args()

    game = Hangman(length=args.minlength)
    game.minlength = args.minlength
    game.newGame()


if __name__ == "__main__":
    main()


