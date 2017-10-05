# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle


import random

# Empty tile, there's only one empty cell on a field:

EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.

MOVES = {
    'w': - 4,
    's': 4,
    'a': - 1,
    'd': 1,
}


def shuffle_field():
    task = []
    for i in range(1, 16):
        task.append(i)
    task.append(EMPTY_MARK)
    random.shuffle(task)
    return task


def print_field(num):
    a = 0
    while (a < len(num)):
        print(num[a], num[a + 1], num[a + 2], num[a + 3])
        a += 4


def is_game_finished(field):
    field_check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']
    if field_check == field:
        return True
    else:
        return False


def handle_user_input():
    move = input('Input direct:')
    if (move in MOVES or move == 'End'):
        return move
    else:
        return False


def perform_move(fiel, key):
    number = MOVES[key]
    locate = fiel.index('x')
    fiel[locate], fiel[locate + number] = fiel[locate + number], fiel[locate]
    return fiel


def main():
    result_list = shuffle_field()
    step = 0
    print_field(result_list)
    while(is_game_finished(result_list) is False):
        act = handle_user_input()
        try:
            index = result_list.index('x')
            if(act and act != 'End'):
                if(index >= 0 and index < 4 and act == 'w'):
                    print('No move')
                elif(index >= 12 and index < 16 and act == 's'):
                    print('No move')
                elif((index + 1) % 4 == 0 and act == 'd'):
                    print('No move')
                elif((index % 4 == 0 or index == 0) and act == 'a'):
                    print('No move')
                else:
                    result_list = perform_move(result_list, act)
                    step += 1
                    print_field(result_list)
            else:
                print('Uncorrect data')
        except IndexError:
            print('No move')

    if(is_game_finished(result_list)):
        print('You win!')
        print('Steps:', step)

try:
    main()
except KeyboardInterrupt:
    print('shutting down')