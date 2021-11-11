"""
Hangman style game with Python
themed words to be guessed
"""
import random
import sys
from py_words import words_list


class ColorText:
    """
    Changes colors of text based on
    correct & incorrect input
    """
    BOLD = '\033[1m'
    CYAN = '\033[36m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    WHITE = '\033[0m'


# Intro text about the game and how to play.
print(f"     {ColorText.BOLD}{ColorText.YELLOW}Welcome to the PY MAN game!"
      f"{ColorText.BOLD}{ColorText.WHITE}")
print("     You may have guessed this is a Python themed game (^_^)")
print("     Rules are same as in the traditional Hangman. You have 6 lives.")
print("     You will type in letters which you think are part of the word.")
print("     Only single alphabetical characters are allowed.")
print("     Good luck!")
print("                             .::::::::::.")
print("                            .::``::::::::::.")
print("                            :::..:::::::::::")
print("                            ````````::::::::")
print("                    .::::::::::::::::::::::: iiiiiii,")
print("                 .:::::::::::::::::::::::::: iiiiiiiii.")
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
        delete_last_line()
        print(f"     {user_choice}")

    else:
        user_choice = "Y"

    while len(user_choice) == 0:
        if len(user_choice) == 0:
            print(f"\n     Invalid input - only type {ColorText.BOLD}"
                  f"{ColorText.YELLOW} Y for yes{ColorText.WHITE}"
                  f" or type {ColorText.BOLD}{ColorText.YELLOW} "
                  f"N for no{ColorText.WHITE}\n     ---\n")
            user_choice = input("\n     Are you ready to play?"
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
            else:
                # if user puts any other character than Y or N,
                # it will print 'Invalid Input' and it will
                # reprint user choice command line.
                print(f"\n     Invalid input - only type {ColorText.BOLD}"
                      f" {ColorText.YELLOW}Y for yes "
                      f" {ColorText.BOLD}{ColorText.WHITE} "
                      f"or type {ColorText.BOLD}{ColorText.YELLOW}N for "
                      f"no{ColorText.BOLD}{ColorText.WHITE}\n     ---\n")
            user_choice = input("\n     Are you ready to "
                                "play? (Y/N)\n     "
                                "---\n").upper()
            delete_last_line()
            print(f"     {user_choice}")

    play_word = get_random_word().upper()
    play_word_set = set()
    for letter in play_word:
        play_word_set.add(letter)
    print(play_word_set)
    print(len(play_word_set))
    print(play_word)
    masked_word = "_" * len(play_word)
    # masked_word = [guessed for guessed in play_word]
    incorrect_attempts = 6
    guessed = []  # list of correctly guessed letters
    incorrect = []  # list of incorrectly guessed letters
    correct = False
    print(f"     {ColorText.BOLD}{ColorText.CYAN}PY word:{ColorText.WHITE}"
          f" " + " ".join(masked_word) + "\n")
    print(f"\n     .....................\n     You have {incorrect_attempts}"
          " lives left\n     .....................\n")

    while incorrect_attempts > 0:
        if len(guessed) == len(play_word_set):
            correct = True
            print(f"\n     Well done! {ColorText.BOLD}{ColorText.GREEN}"
                  f"{play_word}{ColorText.BOLD}"
                  f" {ColorText.WHITE} is correct!\n     ...\n")
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
                print(f"\n     {ColorText.YELLOW}You already tried"
                      f" '{letter}'.\n     ---\n{ColorText.WHITE}")
            elif len(letter) != 1 or not letter.isalpha():
                print(f"\n     {ColorText.YELLOW}Only one alphabetical"
                      f" character allowed at time.\n"
                      f"     ---\n{ColorText.WHITE}")
            elif incorrect_attempts == 1:
                print(f"\n     {ColorText.BOLD}{ColorText.CYAN}PY word: "
                      f"{ColorText.WHITE} " + " ".join(masked_word) + "\n")
                print(f"\n     The correct word was {ColorText.BOLD}"
                      f"{ColorText.YELLOW}{play_word}{ColorText.WHITE}.")
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
                guessed.append(letter)  # adds the guessed letter into a list
                masked_word = [
                    # shows underscores as placements for letters
                    # if letter is correct, letter replaces underscore
                    letter if letter in guessed
                    else '_' for letter in play_word]
                # masked_word_list = list(masked_word)
                # indices = [i for i, guess in enumerate(play_word)
                #            if guess == letter]
                # for index in indices:
                #     masked_word_list[index] = letter
                #     masked_word = "".join(masked_word_list)
                print(f"\n     {ColorText.GREEN} Great, '{letter}' "
                      f"is in the word.\n     ---\n{ColorText.WHITE}")
                print(f"\n     {ColorText.BOLD}{ColorText.CYAN}PY word: "
                      f"{ColorText.WHITE} " + "".join(masked_word) + "\n")
            else:
                incorrect_attempts -= 1
                incorrect.append(letter)
                # adds the incorrectly guessed letter into a list
                print(f"\n     {ColorText.RED}'{letter}' "
                      f"is not in the word.\n     ---\n{ColorText.WHITE}")
                print(f"\n     .....................\n     You have "
                      f"{incorrect_attempts} lives left"
                      f"\n     .....................")
                print(f"\n     {ColorText.BOLD}{ColorText.CYAN}PY word: "
                      f"{ColorText.WHITE} " + " ".join(masked_word) + "\n")


def restart():
    """
    Function to restart the game
    """
    user_choice = input("     Would you like to play again?"
                        " (Y/N)\n     ---\n").upper()

    while len(user_choice) == 0:
        if len(user_choice) == 0:
            print(f"\n     Invalid input - only type {ColorText.BOLD}"
                  f"{ColorText.YELLOW} Y for yes {ColorText.WHITE}"
                  f"or type {ColorText.BOLD}{ColorText.YELLOW} "
                  f"N for no{ColorText.WHITE}\n     ---\n")
            user_choice = input("     Would you like to play again?"
                                " (Y/N)\n     ---\n").upper()
            delete_last_line()
            print(f"     {user_choice}")

    else:
        while len(user_choice) >= 1:
            if user_choice == "Y":
                delete_last_line()
                # print("     YES\n")
                play(False)
                break
            elif user_choice == "N":
                delete_last_line()
                print('     NO')
                print("\n     Thanks for playing, see you soon!\n")
                raise SystemExit
            else:
                # if user puts any other character than Y or N,
                # it will print 'Invalid Input' and it will
                # reprint user choice command line.
                print(f"\n     Invalid input - only type {ColorText.BOLD}"
                      f" {ColorText.YELLOW}Y for yes "
                      f" {ColorText.BOLD}{ColorText.WHITE} "
                      f"or type {ColorText.BOLD}{ColorText.YELLOW}N for "
                      f"no{ColorText.BOLD}{ColorText.WHITE}\n     ---\n")
            user_choice = input("     Would you like to play again?"
                                " (Y/N)\n     ---\n").upper()
            delete_last_line()
            print(f"     {user_choice}")


def main():
    """
    Runs the game
    """
    play()


main()
