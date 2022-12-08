import random
import os
from time import sleep
from words import words

# import json


class colors:
    RED = "\033[1;31m"
    GREEN = "\033[0;32m"
    CYAN = "\033[1;36m"
    RESET = "\033[0;0m"


def game_intro():
    """
    Game intro function that prints the title art and
    welcomes the user, request the name and print Welcome name.
    """
    print_title()
    while True:
        name = input("Please enter your name:\n")

        if not name.isalpha():
            print(
                f"{colors.RED}Please enter your name"
                f" using letters only.\n {colors.RESET}"
            )
            continue
        else:
            sleep(0.5)
            print(f"Welcome, {name}! Are you ready to be hanged?")
            break


def initialise_game(random_word):
    """
    Function that offers a user two choices:
    1. play the game
    2. read the rules

    Args:
        random_word (string): generates a random word to play the game

    Returns:
        _type_: _description_
    """
    print("Press P to play the game")
    print("Press R to view the rules of the game.")
    start = False
    while not start:
        choice = input(("\n")).upper()
        if choice == "P":
            start = True
            play(random_word)
        elif choice == "R":
            game_rules()
            input(
                f"{colors.GREEN}Please press Enter"
                f" to return to the Menu\n{colors.RESET}"
            )
            os.system('clear')
            print_title()
            return initialise_game(random_word)
        else:
            print("Please make a valid choice.")


def game_rules():
    """
    Prints the game rules to the user
    """
    print("How to play:")
    print("This is a guess word game.")
    print("Guess one letter at a time or whole word if you feel lucky.")
    print("If your guess is wrong, you loose a life.")
    print("When you reach 0 lives, I win and you will be hanged!")
    print("If you guess all letters or a word correctly, you win!")
    print("Good luck!")


# def get_word():
#     """Get a random word and return

#     Returns:
#         string, random word
#     """
#     with open("words.json", "r") as f:
#         word = json.load(f)
#     return random.choice(word).upper()
def get_word():
    """
    Get a random word and return
    """
    random_word = random.choice(words)
    return random_word.upper()


def play(random_word):
    """
    Function that runs the game
    Prints welcome message, hangman and word to guess
    Checks if guess is correct and returns appropriate message
    """
    word_to_guess = ("_" * len(random_word)).rstrip()
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 10
    os.system('clear')
    print(random_word)
    print("Welcome to The Hangman! \nLet's play!")
    print(print_hangman(lives))
    print(f"{colors.GREEN}You have {lives} lives left{colors.RESET}")
    print(word_to_guess)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            os.system('clear')
            if guess in guessed_letters:
                print(f"You already guessed letter {guess}")
                print(f"You have already guessed: {guessed_letters}")
            elif guess not in random_word:
                os.system('clear')
                print(
                    f"{colors.RED}Letter {guess}"
                    f" is not in the word. Try again.{colors.RESET}"
                )
                lives -= 1
                guessed_letters.append(guess)
                print(f"You have already guessed: {guessed_letters}")
            else:
                os.system('clear')
                print(f"{colors.GREEN}Amazing! {guess}"
                      f" is in the word!{colors.RESET}")
                guessed_letters.append(guess)
                print(f"You have already guessed: {guessed_letters}")
                word_list = list(word_to_guess)
                indices = [i for i, letter in enumerate(random_word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                word_to_guess = "".join(word_list)
                if "_" not in word_to_guess:
                    guessed = True
        elif len(guess) == len(random_word) and guess.isalpha():
            os.system('clear')
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != random_word:
                os.system('clear')
                print(f"{colors.RED}{guess} is not the word.{colors.RESET}")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_to_guess = random_word
        else:
            os.system('clear')
            print(f"{colors.RED}Not a valid guess{colors.RESET}")
            print(f"You have already guessed: {guessed_letters}")
        print(print_hangman(lives))
        print(f"{colors.GREEN}You have {lives} lives left{colors.RESET}")
        print(word_to_guess)
        print("\n")
    if guessed:
        os.system('clear')
        print(
            f"{colors.GREEN}Congratulations!"
            f" You guessed the word! You win!{colors.RESET}"
        )
        you_win()
    else:
        os.system('clear')
        print(
            f"{colors.RED}Sorry, you ran out of tries."
            f" The word was {random_word}."
            f" Better luck next time!{colors.RESET}"
        )
        game_over()


def print_hangman(lives):
    """
    Displays hangman depending on number of wrong guesses
    """
    lives_left = [
        """
    |----+
    O    |
   /|\   |
   / \   |
        ===
        """,
        """
    |----+
    O    |
   /|\   |
   /     |
        ===
        """,
        """
    |----+
    O    |
   /|\   |
         |
        ===
        """,
        """
    |----+
    O    |
   /|    |
         |
        ===
        """,
        """
    |----+
    O    |
    |    |
         |
        ===
        """,
        """
    |----+
    O    |
         |
         |
        ===
        """,
        """
    |----+
         |
         |
         |
        ===
        """,
        """
       --+
         |
         |
         |
        ===
        """,
        """
         +
         |
         |
         |
        ===
        """,
        """


         |
         |
        ===
        """,
        """




        ===
        """,
    ]
    return lives_left[lives]


def print_title():
    """
    Fucntion to print the title
    """
    print(f"{colors.CYAN}   _______ _            _    _{colors.RESET}")
    print(f"{colors.CYAN}  |__   __| |          | |  | |")
    print(
        f"{colors.CYAN}     | |  | |__   ___  | |__| | __ _ _ __   __ _ _ __ "
        f"___   __ _ _ __{colors.RESET}"
    )
    print(
        f"{colors.CYAN}     | |  | '_ \ / _ \ |  __  |/ _` | '_ \ / _` | '_ ` "
        f"_ \ / _` | '_ \ {colors.RESET}"
    )
    print(
        f"{colors.CYAN}     | |  | | | |  __/ | |  | | (_| | | | | (_| | | | "
        f"| | | (_| | | | |{colors.RESET}"
    )
    print(
        f"{colors.CYAN}     |_|  |_| |_|\___| |_|  |_|\__,_|_| |_|\__, |_| |_"
        f"| |_|\__,_|_| |_|{colors.RESET}"
    )
    print(
        f"{colors.CYAN}                                            __/ "
        f"|{colors.RESET}"
    )
    print(
        f"{colors.CYAN}                                           |___"
        f"/ {colors.RESET}"
    )


def you_win():
    """
    Function to print You Win when user wins the game
    """
    print(f"{colors.GREEN}__   __            _    _ _{colors.RESET}")
    print(f"{colors.GREEN}\ \ / /           | |  | (_){colors.RESET}")
    print(f"{colors.GREEN} \ V /___  _   _  | |  | |_ _ __{colors.RESET}")
    print(f"{colors.GREEN}  \ // _ \| | | | | |/\| | | '_ \ {colors.RESET}")
    print(f"{colors.GREEN}  | | (_) | |_| | \  /\  / | | | |{colors.RESET}")
    print(f"{colors.GREEN}  \_/\___/ \__,_|  \/  \/|_|_| |_|{colors.RESET}")
    print("\n")


def game_over():
    """
    Function to print Game Over when user loose the game
    """
    print(f"{colors.RED}  _____                        "
          f"_____{colors.RESET}")
    print(
        f"{colors.RED} | |  \/ __ _ _ __ ___   ___  | | | |_   "
        f"_____ _ __{colors.RESET}"
    )
    print(
        f"{colors.RED} | | __ / _` | '_ ` _ \ / _ \ | | | \ \ "
        f"/ / _ \ '__|{colors.RESET}"
    )
    print(
        f"{colors.RED} | |_\ \ (_| | | | | | |  __/ \ \_/ /\ V "
        f"/  __/ |{colors.RESET}"
    )
    print(
        f"{colors.RED}  \____/\__,_|_| |_| |_|\___|  \___/  \_/ "
        f"\___|_|{colors.RESET}"
    )
    print("\n")


def main():
    """
    Function that runs all functions and offer user to choose to play again.
    """
    game_intro()
    random_word = get_word()
    initialise_game(random_word)
    while input("Play again? (Y/N) ").upper() == "Y":
        random_word = get_word()
        play(random_word)


if __name__ == "__main__":
    main()
