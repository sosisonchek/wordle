import json
import random
from termcolor import colored
from subprocess import run
import os


TRIES = 5
MATCH = 'green'
WRONG = 'dark_grey'
MISS  = 'yellow'


with open('wordles.json', 'r') as file:
    wordle_list = json.load(file)

def cli(last_words):

    if os.name == 'nt': run('cls', shell=True)
    else: run('clear', shell=True)
    print('Wordle')
    print('------')

    for word in last_words:

        result = [''] * len(wordle)
        remaining = list(wordle)

        for i in range(len(wordle)):
            if word[i] == wordle[i]:
                result[i] = colored(word[i], MATCH)
                remaining[i] = None

        for i in range(len(wordle)):
            if result[i] != '': continue

            if word[i] in remaining:
                result[i] = colored(word[i], MISS)
            else:
                result[i] = colored(word[i], WRONG)
        
        for char in result:
            print(char, end='')
        print()
        


while True:
    lost = True
    wordle = random.choice(wordle_list)
    last_words = []
    for i in range(TRIES):
        cli(last_words)
        while True:
            user = input('> ')
            user = user.lower()
            if user in wordle_list:
                break
            else: print(f'There\'s no such word as {user}')
        last_words.append(user)
        if user == wordle:
            cli(last_words)
            print('You won! Press enter to start a new round.', end='')
            input()
            lost = False
            break
    if lost:
        print(f'The correct word was {colored(wordle, MATCH)}. Press enter to start a new round.', end='')
        input()
        
