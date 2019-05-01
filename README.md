# hangman_sam

This code runs a game of hangman from the command line!

## How the code works
This hangman game was written with python 3.6 and uses a class
to store game information and run the game. 

The game uses 7 imported libraries:
<ol>
<li><b>pathlib</b> to check for the .txt file in the openFile method</li>
<li><b>urllib</b> to fetch the .txt file if unavailable locally in the openFile method</li>
<li><b>random</b> to select a random word in the wordPick method</li>
<li><b>string</b> to store a lowercase alphabet in the newGame method</li>
<li><b>copy</b> to copy a variable in the newGame method</li>
<li><b>time</b> to pause after the game prints something for game flow in the newGame method</li>
<li><b>argparse</b> to intake command line parameters in the driver code</li>
</ol>

The class has 5 methods:

`__init__()` which initializes the class variables and intakes the games
length argument (explained below).

`openFile()` which checks for a .txt file locally and downloads
the file if it does not exist.

`wordPick()` which selects a random word of at least a minimum length
designated by the user.

`printHangman()` which intakes the number of wrong guesses and prints the
 current state of the game to the user.

`newGame()` which  calls the `openFile` and `wordPick` functions before
in-taking users guesses, indicating if they are in the selected word,
printing out the word in it's un-guessed form, and looping until the
game is over.

The file also has a driver function `main()` that is called using `if __name__ == "__main__":`
allowing the game to be driven by another script if needed. The driver function calls the
initializes the class and calls the `newGame()` method.

### How to Play

Call the game from the command line by navigating to the directory
where _hangman.py_ is saved in and call the following command:
```
>>>py -3.7 hangman.py -l <minimum length of word>
```
The command is telling python to run the file using python version 3.7
`py -3.7 hangman.py` with a length argument `-l`. The length argument is 
required to tell the game the shortest word you want to guess. The file
must be run with python 3.6 or higher.

After running the command with a valid length input (positive integer) the 
game will select a word and display the number of blank spaces in the word
as well as a list of letters to guess from. 
```
 _  _  _  _  _  _  _  _  _
a b c d e f g h i j k l m n o p q r s t u v w x y z
Choose a letter:
```
The game won't accept any input that isn't a letter from the list displayed!

```
Please pick one letter from the list...
```
```
"1" is not a letter! Try again...
```

After making a valid guess the game will indicate whether the guess is in the
word or not and print out the hangman gallows. If you make the same guess more than once
the game will tell you and make you guess again.
```
r is not in the word!
```
```
a is in the word!
```
```
You already guessed "a"!
```

Be careful, you only get 6 wrong guesses before you lose!

```
  |‾‾‾‾‾‾‾|
  |       O
  |      /|\
  |      / \
__|__

 a  _  _  e  l  l  a  _  _
You lose!
The word was appellant
```
After guessing the word and winning, or not guessing the word and losing 
the game will prompt you if you would like to play again. Enter `y` to get
a new word to guess or enter `n` to end the game and exit.
```
Play again? (y/n)
```

