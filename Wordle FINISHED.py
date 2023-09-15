## JOHN NOVATSCOU 20099074
## NMTAFE STUDENT 2023
## Class A

import random
print('Welcome to my Wordle game!')
print('You have 6 guesses to guess the corret word')
print('X = miss, O = misplaced, I = exact')
print('Good Luck!')
max_tries = 6

target_file_name = './word-bank/target_words.txt'
target_file_handle = open(target_file_name)

valid_file_name = './word-bank/all_words.txt'
valid_file_handle = open(valid_file_name)

target_words_list = []
for target_word in target_file_handle:
    target_words_list.append(target_word.rstrip())
target_word = random.choice(target_words_list)

valid_words_list = []
for valid_word in valid_file_handle:
    valid_words_list.append(valid_word.rstrip())

while max_tries > 0:
    guess_word = input('Write guess here: ').lower()
    
        # --- test ---
    #target_word = 'igloo'
    #target_list = list(target_word)
    
    if guess_word not in valid_words_list:
        max_tries = max_tries - 1
        print('Word invalid, please try again')
        continue

    # if guess_word in target_words_list:
    #     max_tries = max_tries - 1

    guess_word.split()

    target_list = list(target_word)
    score_list = [0, 0, 0, 0, 0]

    position = 0

    for guess_letter in guess_word:
        if guess_letter in target_list:
            if target_list[position] == guess_letter:
                score_list[position] = 2
            else:
                score_list[position] = 1
        else:
            score_list[position] = 0

        position += 1


    new_score_list = ''

    for mark in score_list:
        if mark == 2:
            new_score_list += 'I'
        elif mark == 1:
            new_score_list += 'O'
        else:
            new_score_list += 'X'

    print(*guess_word.upper())    
    print(*new_score_list)
    
    if guess_word == target_word:
        print('Victory Achieved!')
        max_tries = 0
    
    max_tries = max_tries - 1

if guess_word != target_word:
    print('Target word:', target_word)

print('Game Over')