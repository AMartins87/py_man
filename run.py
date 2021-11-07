"""
Hangman style game with Python
themed words to be guessed
"""
import random
from py_words import words_list

# Intro text about the game and how to play.
print("     Welcome to the PY MAN game!")
print("     You may have guessed this is a Python themed game (^_^)")
print("     Rules are same as in the traditional Hangman.")
print("     You will type in letters which you think are part of the word.")
print("     Only single alphabetical characters are allowed.")
print("     You have 6 lives. Good luck!")
print("\n")
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
print("\n")


def get_random_word():
    """
    This function picks a random word from
    py_words file
    """
    play_word = random.choice(words_list)
    return play_word.upper()


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
            raise SystemExit
        else:   # if user puts any other character than Y or N,
            # it will print 'Invalid Input' and it will
            # reprint user choice command line.
            print("\nInvalid input - only type Y for yes or press enter,"
                  " or type N for no\n---\n")
            user_choice = input("\nReady to play? (Y/N)\n---\n").upper()

    play_word = get_random_word().upper()
    print(play_word)
    correct_let = "_" * len(play_word)
    incorrect_attempts = 6
    print(f"\n......\nYou have {incorrect_attempts} lives left\n......\n")
    guessed = []  # list of correctly guessed letters
    incorrect = []  # list of incorrectly guessed letters
    correct = False

    while incorrect_attempts > 0:
        if len(guessed) == len(play_word):
            correct = True
            print(f"\nWell done! {play_word} is correct!\n")
            break
        if not correct:
            letter = input("\nGuess a letter:\n---\n").upper()
            if letter in guessed or letter in incorrect:
                print(f"\nYou already tried '{letter}'.\n---\n")
            elif len(letter) != 1 or not letter.isalpha():
                print("\nOnly one alphabetical character"
                      " allowed at time.\n---\n")
            elif letter not in play_word and incorrect_attempts == 0:
                play_again()
            elif letter in play_word:
                guessed.append(letter)  # adds the guessed letter into a set
                correct_let = [
                    # shows underscores as placements for letters
                    # if letter is correct, letter replaces underscore
                    letter if letter in guessed
                    else '_' for letter in play_word]
                print(f"\nGreat, '{letter}' is in the word.\n---\n")
                print('\nPY word: ', ' '.join(correct_let))
            else:
                incorrect_attempts -= 1
                incorrect.append(letter)
                # adds the incorrectly guessed letter into a set
                print(f"\n'{letter}' is not in the word.\n---\n")
                print(f"\n......\nYou have {incorrect_attempts}"
                      " lives left\n......\n")


def quit_game():
    """Takes user to an end of game screen
    if they decide not to play again
    """
    # print("\nThanks for playing, see you soon!\n")


def play_again():
    """
    Function to restart the game
    """
    print("\n You lossssssssst, the python got you !!!")
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
    print("\n")
    user_choice = input("Would you like to play again? (Y/N)\n---\n").upper()
    while user_choice:
        if user_choice == "Y":
            play()
            break
        elif user_choice == "N":
            print("\n No worries, see you soon!\n")
            raise SystemExit
        else:  # if user puts any other character than Y or N,
            # it will print 'Invalid Input' and it will
            # reprint user choice command line.
            print("\nInvalid input - only type Y for yes or press enter,"
                  " or type N for no\n---\n")
            user_choice = input("\n Would you like"
                                " to play? (Y/N)\n---\n").upper()


def main():
    """
    Run all program functions
    """
    play()
    play_again()
    exit()


main()
