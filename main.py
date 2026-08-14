from sharing import *
from termcolor import colored
from subprocess import run
import os
import json
import random


TRIES = 6
MATCH = 'green'
WRONG = 'dark_grey'
MISS  = 'yellow'

language = input('Choose wordle\'s language (en/ru): ')
if language != ('ru' or 'en'): language = 'en'

filepath = os.path.join('langs', f'{language}.json')
with open(filepath, 'r', encoding='UTF-8') as file:
    wordle_list = json.load(file)



def clear():
    if os.name == 'nt': run('cls', shell=True)
    else: run('clear', shell=True)
    print('Wordle')
    print('------')


def wordinput(prefix: str, n_chars=5) -> str:
    while True:
        if prefix != None:
            print(prefix, end=' ')
        word = input().lower()
        if word in wordle_list and len(word) == n_chars:
            break
        else: print('This word is not in the possible wordle answer list')
        print()
    return word

def game(wordle, tries):
    last_words = []
    history = []
    won = False
    for n in range(tries):

        clear()
        for word in history:
            for letter in word:
                print(letter, end='')
            print()
        if won:
            print('You won! Press enter to exit')
            input()
            exit()
        history = []
        guess = wordinput('>')
        if guess == wordle: won = True

        last_words.append(guess)
        
        colored_word = [''] * len(wordle)
        remaining = list(wordle)

        for word in last_words:
            colored_word = [''] * len(wordle)
            remaining = list(wordle)

            for i in range(len(wordle)):
                if word[i] == wordle[i]:
                    colored_word[i] = colored(word[i], MATCH)
                    remaining[i] = None

            for i in range(len(wordle)):
                if colored_word[i] != '':
                    continue
                if word[i] in remaining:
                    colored_word[i] = colored(word[i], MISS)
                else:
                    colored_word[i] = colored(word[i], WRONG)
            history.append(colored_word)
    if not won:
        print(f'You lost! The correct word was {wordle}. Press enter to exit!')
        input()
        exit()
        

while True:
    clear()
    print("""
What do you want to do?
1) Play wordle
2) Share a wordle
3) Play a shared wordle
""")
    gamemode = int(input('> '))
    match gamemode:
        case 1:
            wordle = random.choice(wordle_list)
        case 2: 
            print(f'Encoded wordle: {encode(wordinput('Choose a word:'))}. Press enter to continue')
            input()
            continue
        case 3:
            wordle = decode(input('Enter the code you recieved: '))
    clear()
    game(wordle, TRIES)

    