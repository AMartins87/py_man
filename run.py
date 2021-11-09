"""
Hangman style game with Python
themed words to be guessed
"""
import random
import sys
from py_words import words_list


class ColourText:
    """
    Changes colors of text based on
    correct & incorrect input
    """
    BOLD = '\033[1m'
    WHITE = '\033[0m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'


# Intro text about the game and how to play.
print(f"     {ColourText.BOLD}{ColourText.YELLOW}Welcome to the PY MAN game!"
      f"{ColourText.BOLD}{ColourText.WHITE}")
print("     You may have guessed this is a Python themed game (^_^)")
print("     Rules are same as in the traditional Hangman.")
print("     You will type in letters which you think are part of the word.")
print("     Only single alphabetical characters are allowed.")
print("     You have 6 lives. Good luck!")
print("                             .::::::::::.")
print("                            .::``::::::::::.")
print("                            :::..:::::::::::")
print("                            ````````::::::::")
print("                    .::::::::::::::::::::::: iiiiiii,")
print("                 .:::::::::::::::::::::::::: iiiiiiiii.")
print("                 ::::::::::::::::::::::::::: iiiiiiiiii")
print("                 ::::::::::::::::::::::::::: iiiiiiiiii")
print("                 :::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii")
print("                 `::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii`")
print("                    `:::::: iiiiiiiiiiiiiiiiiiiiiii`")
print("                            iiiiiiii,,,,,,,,")
print("                            iiiiiiiiiii''iii")
print("                            `iiiiiiiiii..ii`")
print("                              `iiiiiiiiii`")


def get_random_word():
    """
    This function picks a random word from
    py_words file
    """
    play_word = random.choice(words_list)
    return play_word.upper()


get_random_word()


# This function has been created by a coder on stackoverflow.com
# Due credit given in README.md file
def delete_last_line():
    '''
    Use this function to delete the last line in the STDOUT
    '''
    # cursor up one line
    sys.stdout.write('\x1b[1A')

    # delete last line
    sys.stdout.write('\x1b[2K')


def play(first_play=True):
    """
    This function starts the application
    """
    if first_play:
        user_choice = input("\n     Are you ready to play?"
                            " (Y/N)\n     ---\n").upper()
    else:
        user_choice = "Y"

    if len(user_choice) == 0:
        print(f"\n     Invalid input - only type {ColourText.BOLD}"
              f"{ColourText.YELLOW} Y for yes {ColourText.WHITE}"
              f" or type {ColourText.BOLD}{ColourText.YELLOW} "
              f"N for no{ColourText.WHITE}\n     ---\n")
        user_choice = input("\n     Ready to play?"
                            " (Y/N)\n     ---\n").upper()
        delete_last_line()
        print(f"     {user_choice}")
    else:
        while len(user_choice) >= 1:
            if user_choice == "Y":
                delete_last_line()
                print("     YES\n")
                get_random_word()
                break
            elif user_choice == "N":
                delete_last_line()
                print('     NO')
                print("\n     Too bad, maybe next time!\n")
                raise SystemExit
            else:   # if user puts any other character than Y or N,
                # it will print 'Invalid Input' and it will
                # reprint user choice command line.
                print(f"\n     Invalid input - only type {ColourText.BOLD}"
                      f" {ColourText.YELLOW}Y for yes "
                      f" {ColourText.BOLD}{ColourText.WHITE} or"
                      f"or type {ColourText.BOLD}{ColourText.YELLOW}N for "
                      f"no{ColourText.BOLD}{ColourText.WHITE}\n     ---\n")
                user_choice = input("\n     Ready to play?"
                                    " (Y/N)\n     ---\n").upper()
                delete_last_line()

    play_word = get_random_word().upper()
    # play_word = []
    print(play_word)
    correct_let = "_" * len(play_word)
    incorrect_attempts = 6
    print(f"\n     ......\n     You have {incorrect_attempts}"
          " lives left\n     ......\n")
    guessed = []  # set of correctly guessed letters
    incorrect = []  # set of incorrectly guessed letters
    correct = False

    while incorrect_attempts > 0:
        if len(guessed) == len(play_word):
            correct = True
            print(f"\n     Well done! {ColourText.BOLD}{ColourText.GREEN}"
                  f"{play_word}{ColourText.BOLD}"
                  f" {ColourText.WHITE} is correct!\n     ......\n")
            print(r"""
                           _
                          /(|
                         (  :
                       __ \ `\_____
                     (____)   |
                    (____)|   |
                     (___).___|
                      (__)___.|___


            """)
            restart()
        if not correct:
            letter = input("\n     Guess a letter:\n     ---\n").upper()
            delete_last_line()
            print(f"     {letter}")
            if letter in guessed or letter in incorrect:
                print(f"\n     You already tried '{letter}'.\n     ---\n")
            elif len(letter) != 1 or not letter.isalpha():
                print("\n     Only one alphabetical character"
                      " allowed at time.\n     ---\n")
            elif incorrect_attempts == 1:
                print(f"\n     The correct word was {ColourText.BOLD}"
                      f"{ColourText.YELLOW}{play_word}{ColourText.BOLD}"
                      f"{ColourText.WHITE}.")
                print("\n     You lossssssssst, the python got you !!!")
                print(r"""
                            /^\/^\
                          _|__|  O|
                    \/      /~  \_/\
                     \___|________/ \
                         \_______    \
                                 \    \
                                 /    /                          \
                                /    /                            \
                               /    /            _----_           \\
                              /    /         _-~       ~-_         \\
                             (    (       -~      _--_    ~-_      / |
                              \    ~-____~-     -~     ~-_    ~-_ / /
                               \            -~            -~       /
                                 ~---____-~                 ~-___-

                    """)
                restart()
            elif letter in play_word:
                guessed.append(letter)  # adds the guessed letter into a set
                correct_let = [
                    # shows underscores as placements for letters
                    # if letter is correct, letter replaces underscore
                    letter if letter in guessed
                    else '_' for letter in play_word]
                print(f"\n     {ColourText.GREEN} Great, '{letter}' "
                      f"is in the word.\n     ---\n{ColourText.WHITE}")
                print('\n     PY word: ', ' '.join(correct_let))
            else:
                incorrect_attempts -= 1
                incorrect.append(letter)
                # adds the incorrectly guessed letter into a set
                print(f"\n     {ColourText.RED}'{letter}' "
                      f"is not in the word.\n     ---\n{ColourText.WHITE}")
                print(f"\n     ......\n     You have {incorrect_attempts}"
                      " lives left\n     ......\n")


def restart():
    """
    Function to restart the game
    """
    user_choice = input("     Would you like to play again? "
                        "(Y/N)\n     ---\n").upper()
    if len(user_choice) == 0:
        print(f"\n     Invalid input - only type {ColourText.BOLD}"
              f"{ColourText.YELLOW} Y for yes {ColourText.WHITE}"
              f" or type {ColourText.BOLD}{ColourText.YELLOW} "
              f"N for no{ColourText.WHITE}\n     ---\n")
        user_choice = input("\n     Ready to play?"
                            " (Y/N)\n     ---\n").upper()
        delete_last_line()
        print(f"     {user_choice}")

    while user_choice:
        if user_choice == "Y":
            delete_last_line()
            print("     YES")
            play(False)
            break
        elif user_choice == "N":
            delete_last_line()
            print('     NO')
            print("\n     Thanks for playing, see you soon!\n")
            raise SystemExit
        else:  # if user puts any other character than Y or N,
            # it will print 'Invalid Input' and it will
            # reprint user choice command line.
            print(f"\n     Invalid input - only type {ColourText.BOLD}"
                  f"{ColourText.YELLOW} Y for yes {ColourText.WHITE}"
                  f" or type {ColourText.BOLD}{ColourText.YELLOW} "
                  f"N for no{ColourText.WHITE}\n     ---\n")
            user_choice = input("     Would you like to play again? "
                                "(Y/N)\n     ---\n").upper()


def main():
    """
    Run all program functions
    """
    play()


main()
