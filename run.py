import random
from words import words
# import json


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
    word_to_guess = ('_' * len(random_word)).rstrip()
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    # print(random_word)
    print("Welcome to The Hangman! \nLet's play!")
    print(print_hangman(lives))
    print(word_to_guess)
    print('\n')
    while not guessed and lives > 0:
        guess = input('Please guess a letter or a word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'You already guessed letter {guess}')
            elif guess not in random_word:
                print(f'Letter {guess} is not in the word. Try again.')
                lives -= 1
                guessed_letters.append(guess)
            else:
                print(f'Amazing! {guess} is in the word!')
                guessed_letters.append(guess)
                word_list = list(word_to_guess)
                indices = [i for i, letter in enumerate(random_word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                word_to_guess = ''.join(word_list)
                if "_" not in word_to_guess:
                    guessed = True
        elif len(guess) == len(random_word) and guess.isalpha():
            if guess in guessed_words:
                print(f'You already guessed the word {guess}')
            elif guess != random_word:
                print(f'{guess} is not the word.')
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_to_guess = random_word
        else:
            print('Not a valid guess')
        print(print_hangman(lives))
        print(word_to_guess)
        print('\n')
    if guessed:
        print('Congratulations! You guessed the word! You win!')
    else:
        print(f'Sorry, you ran out of tries. The word was {random_word}. Better luck next time!')


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
        """
    ]
    return lives_left[lives]

def print_title():
    """
    Fucntion to print the title 
    """
    print("   _______ _            _    _")                                         
    print("  |__   __| |          | |  | |")                                        
    print("     | |  | |__   ___  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __")  
    print("     | |  | '_ \ / _ \ |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ") 
    print("     | |  | | | |  __/ | |  | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("     |_|  |_| |_|\___| |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                                            __/ |")                      
    print("                                           |___/ ")


def main():
    """
    Function that runs all functions and offer user to choose to play again. 
    """
    print_title()
    random_word = get_word()
    play(random_word)
    while input('Play again? (Y/N) ').upper() == 'Y':
        random_word = get_word()
        play(random_word)


if __name__ == "__main__":
    main()
