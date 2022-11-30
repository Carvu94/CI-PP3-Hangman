import random 
from words import words

### Choose a random word
randomWord = random.choice(words)

for x in randomWord:
    print('_', end=' ')

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
