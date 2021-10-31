"""
Hangman style game with Python
themed words to be guessed
"""
import random
from py_words import words


def get_random_word(words):
    """
    This function picks a random word from
    py_words file
    """
    play_word = random.choice(words)
    return play_word
# print(get_random_word(words))


def intro():
    """
    This functions starts the application
    and gives a little intro text about the
    game and how to play.
    """
    print("\n")
    print("Welcome to the PY MAN game!")
    print("You may have guessed this is a Python themed game (^_^)")
    print("Rules are same as in the traditional Hangman.")
    print("You will type in letters which you think are part of the word.")
    print("You will have 6 attempts to try and guess the correct word.")
    print("\n")
    print("                        .::::::::::.")
    print("                       .::``::::::::::.")
    print("                       :::..:::::::::::")
    print("                       ````````::::::::")
    print("               .::::::::::::::::::::::: iiiiiii,")
    print("            .:::::::::::::::::::::::::: iiiiiiiii.")
    print("            ::::::::::::::::::::::::::: iiiiiiiiii")
    print("            ::::::::::::::::::::::::::: iiiiiiiiii")
    print("            :::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii")
    print("            `::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii`")
    print("               `:::::: iiiiiiiiiiiiiiiiiiiiiii`")
    print("                       iiiiiiii,,,,,,,,")
    print("                       iiiiiiiiiii''iii")
    print("                       `iiiiiiiiii..ii`")
    print("                         `iiiiiiiiii`")
    print("\n")

    play = input("Are you ready to play? (Y/N)\n")

    if play == "Y":
        play(words)
    elif play == "N":
        print("\nToo bad, maybe next time!\n")
        quit_game()


intro()


def play(words):
    """
    Function to play
    """
    # play_word = get_random_word(words)
    # used_letters = []
    # correct_letters = []


def quit_game():
    """Takes user to an end of game screen
    if they decide not to play again
    """
    print("\nThanks for playing, see you soon!\n")

quit_game()


def play_again():
    """
    Function to restart the game
    """
    pass
