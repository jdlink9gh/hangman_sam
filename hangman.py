import urllib.request
import copy
import random
import pathlib
import time
import argparse
import string

class Hangman():

    def __init__(self, length):     # intaking the length argument from the command line
        self.game_state = 0            # state of the hangman; 1-6
        self.guess = str()          # input from player; 1 alphabetical character
        self.word_list = list()         # list of words read from text file
        self.word = str()           # word chosen by the program
        self.min_length = length     # setting the minimum length of the word chosen by the program to the length arg

    def open_file(self):
        # This method does multiple things. First, it checks if the ./word_data/ directory exists and creates it if it
        # does not exist. Second, it checks if the word.txt file exists in the directory and downloads it if it does
        # not exist. Third, it opens the file and writes the contents to a list.

        # checking and creating the directory if necessary
        pathlib.Path('./word_data/').mkdir(parents=True, exist_ok=True)

        # storing the relative file path to the words.txt file
        file_path = './word_data/words.txt'

        try:
            # checking if the file exists
            with open(file_path) as f:
                print('file exists')
        except FileNotFoundError:
            # downloading the file to the directory if it does not exist
            print('file does not exist')
            url = 'http://norvig.com/ngrams/sowpods.txt'
            urllib.request.urlretrieve(url, file_path)
            print('file downloaded to ' + file_path)
        finally:
            # storing the file contents as a list
            with open(file_path) as f:
                self.word_list = f.readlines()
            print('file read')

    def word_pick(self):
        # This method randomly selects a word of a minimum length from the stored list

        # selecting a random word from the list that has a length greater than the specified minimum
        while len(self.word) < self.min_length:
            self.word = random.choice(self.word_list).lower()[:-1]

    def print_hangman(self, wrong_guesses):
        # This method prints on of the 7 states of the hangman
        # This method prints on of the 7 states of the hangman
        print('  |‾‾‾‾‾‾‾|')  # printing top line of gallows for all states

        if wrong_guesses > 0:  # printing second line of gallows for all states
            print('  |       O')
        else:
            print('  |')

        if wrong_guesses == 6:  # printing third line of gallows for all states
            print('  |      /|\\')
        elif wrong_guesses == 5:
            print('  |      /|')
        elif wrong_guesses >= 2:
            print('  |       |')
        else:
            print('  |')

        if wrong_guesses >= 4:  # printing fourth line of gallows for all states
            print('  |      / \\')
        elif wrong_guesses == 3:
            print('  |      / ')
        else:
            print('  |')

        print('__|____\n')  # printing fifth line of gallows for all states

    def new_game(self):

        self.open_file()
        self.word_pick()

        alphabet = list(string.ascii_lowercase)
        valid_guesses = copy.deepcopy(alphabet)
        made_guesses = ''
        target_word = ''
        displayed_word = ''

        for char in self.word:
            target_word += ' ' + char + ' '

        for _ in self.word:
            displayed_word += ' _ '
        print(displayed_word)

        while self.game_state < 6:
            displayed_word = ''

            print(*valid_guesses, sep=' ')
            guess = input("Choose a letter: ")
            guess = guess.lower()

            if guess in alphabet:
                if guess in valid_guesses:
                    valid_guesses.remove(guess)

                if guess not in made_guesses:
                    made_guesses += guess

                    if guess not in self.word:
                        print(f'{guess} is not in the word!')
                        self.game_state += 1
                    else:
                        print(f'{guess} is in the word!')

                else:
                    print(f'You already guessed "{guess}"!')

                time.sleep(1)
                self.print_hangman(self.game_state)

                for char in self.word:
                    if char in made_guesses:
                        displayed_word += ' ' + char + ' '
                    else:
                        displayed_word += ' _ '

                print(displayed_word)

                if displayed_word == target_word:
                    print(f'You won in {len(made_guesses)} guesses!')
                    break
                elif self.game_state == 6:
                    print(f'You lose!\nThe word was {self.word}')
                    break
            elif len(guess) != 1:
                print("Please pick one letter from the list...")
            else:
                print(f'"{guess}" is not a letter! Try again...')

            time.sleep(.75)

        again = input('Play again? (y/n)')
        if again == 'y':
            self.new_game()
        else:
            print("Thanks for playing!")


def main():
    # driver function if hangman.py is run

    # the next 3 word_list of code setup the CLI input using the argparse library
    parser = argparse.ArgumentParser(description='Play a game of Hangman')
    parser.add_argument('-m', '--min_length', type=int, metavar='', required=True,
                        help='Minimum length of the word you would like to guess')
    args = parser.parse_args()

    game = Hangman(length=args.min_length)
    game.new_game()


if __name__ == "__main__":
    main()


