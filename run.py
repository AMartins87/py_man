"""
Hangman style game with Python
themed words to be guessed
"""
import random
from py_words import words_list


def get_random_word(words_list):
    """
    This function picks a random word from
    py_words file
    """
    play_word = random.choice(words_list)
    return play_word


get_random_word(words_list)


def intro():
    """
    This functions starts the application
    and gives an intro text about the
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
        get_random_word(words_list)
    elif play == "N":
        print("\nToo bad, maybe next time!\n")
        quit_game()


def play():
    """
    Function to play
    """
    play_word = get_random_word(words_list)
    correct_let = "_" * len(play_word)
    attempts = 6
    guessed = incorrect = set()
    correct = False

    while attempts > 0:
        if not correct:
            letter = input("\nGuess a letter:\n")
            if letter in guessed or letter in incorrect:
                print("Invalid input. Try again,")
            elif letter in play_word:
                correct_let = list(correct_let)
                correct_let = "_".join(correct_let)
                guessed.add(letter)
            elif letter not in play_word:
                attempts -= 1
                incorrect.add(letter)
                print("This character is not in the word.")
                if attempts == 0:
                    print("Game over")
        else:
            print(f'"Well done,", {play_word}, "is correct!"')


def quit_game():
    """Takes user to an end of game screen
    if they decide not to play again
    """
    print("\nThanks for playing, see you soon!\n")


def play_again():
    """
    Function to restart the game
    """


def main():
    """
    Run all program functions
    """
    intro()
    play()
    play_again()
    quit_game()


main()
