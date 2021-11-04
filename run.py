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
print("Only single uppercase alphabetical characters are allowed.")
print("You have 6 lives. Good luck!")
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
    user_choice = input("Are you ready to play? (Y/N)\n---\n").upper()
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
            print("\nInvalid input\n---\n")
            user_choice = input("\nReady to play? (Y/N)\n---\n").upper()

    # play_word = get_random_word().upper()
    # print(play_word)
    # correct_let = "_" * len(play_word)
    # incorrect_attempts = 6
    # guessed = set() # set of guessed letters
    # incorrect = set()  # set of incorrectly guessed letters
    # correct = False
    play_word = get_random_word().upper()
    play_word = [i.upper() for i in play_word]
    print(f'\n', *play_word)
    incorrect_attempts = 6
    guessed = ''

    while incorrect_attempts > 0:
        incorrect = 0
        for i in play_word:
            if i in guessed:
                print(i, end=' ')
            else:
                print('_', end=' ')
                incorrect += 1
        if incorrect == 0:
            print("\n\nWell done, you got it! {} is correct" .format(*play_word))
            break
        letter = input("\n\nGuess a letter:\n---\n")
        letter = letter.upper()
        guessed += letter
        if letter not in play_word:
            incorrect_attempts -= 1
            if incorrect_attempts == 0:
                print("\n\nGame over, the PY word was {}".format(*play_word))
            else:
                print(f"\n'{letter}' is not in the word.\n---\n")

    # while incorrect_attempts > 0:
    #   incorrect = 0
    #     if len(guessed) == len(play_word):
    #         correct = True
    #         print(f'\n"Well done,", {play_word}, "is correct!"')
    #         break

    #     if not correct:
    #         letter = input("\nGuess a letter:\n---\n")
    #         if letter in guessed or letter in incorrect:
    #             print(f"\nYou already tried {letter}.\n")
    #         elif letter.islower() or not letter.isalpha():
    #             # if user uses
    #             # lowercase or non-alphabetical character,
    #             # an error message will be printed
    #             print("Type only alphabetical characters in uppercase.\n---\n")
    #         elif letter in play_word:
    #             guessed.add(letter)  # adds the guessed letter into a set
    #             correct_let = [
    #                 # shows underscores as placements for letters
    #                 # if letter is correct, letter replaces underscore
    #                 letter if letter in guessed
    #                 else '_' for letter in play_word]
    #             print("\nGreat, this letter is in the word.\n---\n")
    #             print('\nPY word: ', ' '.join(correct_let))
    #         elif letter not in play_word:
    #             if incorrect_attempts == 0:
    #                 print("\nGame over")
    #                 break
    #             incorrect_attempts -= 1
    #             incorrect.add(letter)
    #             # adds the incorrectly guessed letter into a set
    #             print(f"\n'{letter}' is not in the word.\n---\n")


def quit_game():
    """Takes user to an end of game screen
    if they decide not to play again
    """
    # print("\nThanks for playing, see you soon!\n")


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
