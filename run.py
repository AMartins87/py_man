"""
Hangman style game with Python
themed words to be guessed
"""
import random
from py_words import words_list

# Intro text about the game and how to play.
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


def get_random_word():
    """
    This function picks a random word from
    py_words file
    """
    play_word = random.choice(words_list)
    return play_word


get_random_word()


def play():
    """
    This function starts the application
    """
    user_choice = input("Are you ready to play? (Y/N)\n").upper()
    while user_choice:
        if user_choice == "Y":
            get_random_word()
            break
        elif user_choice == "N":
            print("\nToo bad, maybe next time!\n")
            quit_game()
            break
        else:   # if user puts any other character than Y or N,
            # it will print 'Invalid Input' and it will
            # reprint user choice command line.
            print("Invalid input")
            user_choice = input("\nAre you ready to play? (Y/N)\n").upper()

    play_word = get_random_word()
    correct_let = "_" * len(play_word)
    attempts = 6
    guessed = set()  # these are empty sets
    incorrect = set()  # these are empty sets
    correct = False

    while attempts > 0:
        if not correct:
            letter = input("\nGuess a letter:\n---\n")
            # letter = letter.upper()
            if letter in guessed or letter in incorrect:
                print(f"You already tried {letter}.")
            elif letter in play_word:
                correct_let = list(correct_let)
                correct_let = "_".join(correct_let)
                guessed.add(letter)
                print("\nGreat, this letter is in the word.\n---\n")
            elif letter not in play_word:
                attempts -= 1
                incorrect.add(letter)
                print("\nThis character is not in the word.\n---\n")
                if attempts == 0:
                    print("\nGame over")
                    break
        else:
            print(f'"Well done,", {play_word}, "is correct!"')
            break


def quit_game():
    """Takes user to an end of game screen
    if they decide not to play again
    """
    print("\nThanks for playing, see you soon!\n")


# def play_again():
#     """
#     Function to restart the game
#     """


def main():
    """
    Run all program functions
    """
    play()
    # play_again()
    quit_game()


main()
