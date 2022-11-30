import random
from words import words


def get_word():
    """ 
    Get a random word and return
    """
    randomWord = random.choice(words)
    return randomWord.upper()


# for x in randomWord:
#     print('_', end=' ')


def print_hangman(wrong):
    """
    Prints hangman depending on number of wrong guesses
    """
    if(wrong == 0):
        print('\n|----+')
        print('    |')
        print('    |')
        print('    |')
        print('   ===')
    elif(wrong == 1):
        print('\n|----+')
        print('O   |')
        print('    |')
        print('    |')
        print('   ===')
    elif(wrong == 2):
        print('\n|----+')
        print('O   |')
        print('|   |')
        print('    |')
        print('   ===')
    elif(wrong == 3):
        print('\n|----+')
        print(' O  |')
        print('/|  |')
        print('    |')
        print('   ===')
    elif(wrong == 4):
        print('\n|----+')
        print(' O  |')
        print('/|\ |')
        print('    |')
        print('   ===')
    elif(wrong == 5):
        print('\n|----+')
        print(' O  |')
        print('/|\ |')
        print('/   |')
        print('   ===')
    elif(wrong == 6):
        print('\n|----+')
        print(' O  |')
        print('/|\ |')
        print('/ \ |')
        print('   ===')
