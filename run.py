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
    correct & incorrect input, and helps
    to highlight important info.
    """
    bold = '\033[1m'
    cyan = '\033[36m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    white = '\033[0m'


# Intro text about the game and how to play.
print(f"     {ColorText.bold}{ColorText.yellow}Welcome to the PY MAN game!"
      f"{ColorText.bold}{ColorText.white}")
print("     You may have guessed this is a Python themed game (^_^)")
print("     Rules are same as in the traditional Hangman. You have 5 lives.")
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
    py_words file everytime user plays the game.
    """
    play_word = random.choice(words_list)
    return play_word.upper()


# This function has been created by a coder on stackoverflow.com
# Due credit given in README.md file
def delete_last_line():
    '''
    Use this function to delete the last line in the STDOUT
    '''
    # Cursor up one line
    sys.stdout.write('\x1b[1A')

    # Deletes last line
    sys.stdout.write('\x1b[2K')


def play(first_play=True):
    """
    This function is the main function of the game.
    Contains all the conditions of the game.
    """
    # Argument first_play is used for a first game only.
    # It is not used when user chooses to play again
    # after win or loss.
    if first_play:
        user_choice = input("\n     Are you ready to play?"
                            " (Y/N)\n     ---\n").upper()
        delete_last_line()
        print(f"     {user_choice}")

    else:
        user_choice = "Y"

    while len(user_choice) == 0:
        # This prevents user trying to use enter or spacebar as a character
        if len(user_choice) == 0:
            print(f"\n     Invalid input - only type {ColorText.bold}"
                  f"{ColorText.yellow} Y for yes {ColorText.white}"
                  f"or type {ColorText.bold}{ColorText.yellow} "
                  f"N for no{ColorText.white}\n     ---\n")
            user_choice = input("\n     Are you ready to play?"
                                " (Y/N)\n     ---\n").upper()
            delete_last_line()
            print(f"     {user_choice}")

    else:
        while len(user_choice) >= 1 and user_choice != "Y" or \
              user_choice != "N":
            if user_choice == "Y":
                delete_last_line()
                print("     YES\n")
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
                print(f"\n     Invalid input - only type {ColorText.bold}"
                      f" {ColorText.yellow}Y for yes "
                      f" {ColorText.bold}{ColorText.white} "
                      f"or type {ColorText.bold}{ColorText.yellow}N for "
                      f"no{ColorText.bold}{ColorText.white}\n     ---\n")
                user_choice = input("\n     Are you ready to "
                                    "play? (Y/N)\n     "
                                    "---\n").upper()
                delete_last_line()
                print(f"     {user_choice}")

    play_word = get_random_word().upper()
    play_word_set = set()
    for letter in play_word:
        play_word_set.add(letter)
    masked_word = "_" * len(play_word)
    incorrect_attempts = 5
    guessed = []  # list of correctly guessed letters
    incorrect = []  # list of incorrectly guessed letters
    correct = False
    game_stats(masked_word, incorrect_attempts)

    while incorrect_attempts > 0:
        if len(guessed) == len(play_word_set):
            correct = True
            print(f"\n     Well done! {ColorText.bold}{ColorText.green}"
                  f"{play_word}{ColorText.bold}"
                  f" {ColorText.white} is correct!\n     ...\n")
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
            # Checks if user is entering repeated letters
            if letter in guessed or letter in incorrect:
                print(f"\n     {ColorText.yellow}You already tried"
                      f" '{letter}'.\n     ---\n{ColorText.white}")
            # Checks user is entering only one alphabetical character at time
            elif len(letter) != 1 or not letter.isalpha():
                print(f"\n     {ColorText.yellow}Only one alphabetical"
                      f" character allowed at time.\n"
                      f"     ---\n{ColorText.white}")
                game_stats(masked_word, incorrect_attempts)
            elif letter in play_word:
                # If letter is in the guessed word,
                # this adds the letter into a list
                guessed.append(letter)
                masked_word = [
                    # Shows underscores as placements for letters
                    # If letter is correct, letter replaces underscore
                    letter if letter in guessed
                    else '_' for letter in play_word]
                print(f"\n     {ColorText.green} Great, '{letter}' "
                      f"is in the word.\n     ---\n{ColorText.white}")
                game_stats(masked_word, incorrect_attempts)
            else:
                incorrect_attempts -= 1
                incorrect.append(letter)
                # Adds the incorrectly guessed letter into a list
                print(f"\n     {ColorText.red}'{letter}' "
                      f"is not in the word.\n     ---\n{ColorText.white}")
                game_stats(masked_word, incorrect_attempts)
                if incorrect_attempts == 0:
                    # game_stats(masked_word, incorrect_attempts)
                    print(f"\n     The correct word was {ColorText.bold}"
                          f"{ColorText.yellow}{play_word}{ColorText.white}.")
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


def game_stats(masked_word, incorrect_attempts):
    """"
    This function prints current statistics
    about player's lives left and status
    of the guessed word
    """
    print(f"\n     .....................\n     You have "
          f"{incorrect_attempts} lives left"
          f"\n     .....................")
    print(f"\n     {ColorText.bold}{ColorText.cyan}PY word: "
          f"{ColorText.white} " + " ".join(masked_word) + "\n")


def restart():
    """
    This function will allow users to play
    again if they choose to.
    """
    user_choice = input("     Would you like to play again?"
                        " (Y/N)\n     ---\n").upper()
    delete_last_line()
    print(f"     {user_choice}")

    while len(user_choice) == 0:
        # This prevents user trying to use enter or spacebar as a character
        if len(user_choice) == 0:
            print(f"     {user_choice}")
            print(f"\n     Invalid input - only type {ColorText.bold}"
                  f"{ColorText.yellow} Y for yes {ColorText.white}"
                  f"or type {ColorText.bold}{ColorText.yellow} "
                  f"N for no{ColorText.white}\n     ---\n")
            user_choice = input("     Would you like to play again?"
                                " (Y/N)\n     ---\n").upper()
            delete_last_line()
            print(f"     {user_choice}")

    else:
        while len(user_choice) >= 1 and user_choice != "Y" or \
              user_choice != "N":
            if user_choice == "Y":
                delete_last_line()
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
                print(f"\n     Invalid input - only type {ColorText.bold}"
                      f" {ColorText.yellow}Y for yes "
                      f" {ColorText.bold}{ColorText.white} "
                      f"or type {ColorText.bold}{ColorText.yellow}N for "
                      f"no{ColorText.bold}{ColorText.white}\n     ---\n")
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
