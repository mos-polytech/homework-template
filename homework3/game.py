# -*- coding: utf-8 -*-

import random

# import sys asd

EMPTY_MARK = 'x'  # переменная с х
MOVES = {'w': -4, 's': 4, 'a': -1, 'd': 1, }


def shuffle_field():
    number_for_games = []  # создаем массив
    for i in range(1, 16):  # включаем цикл от 1 до 16
        number_for_games.append(i)  # добавляем  в конец массива
    number_for_games.append(EMPTY_MARK)  # добавляем в конец
    random.shuffle(number_for_games)  # перемешиваем значения
    return number_for_games  # возвращаем значени


def print_field(fields):
    j = 0
    while j < len(fields):
        print(fields[j], fields[j + 1], fields[j + 2], fields[j + 3])
        j += 4


def is_game_finished(field):  # игра закончен
    wins_checks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']
    if field == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']:
        return True  # возвращаем тру
    elif field == wins_checks:  # Если иначе равен
        return True
    else:
        return False


def perform_move(fields, keys):
    key = MOVES[keys]
    index = fields.index('x')
    if (index >= 0 and index < 4 and keys == 'w'):
        print('Выход за  границы')
    elif (index >= 12 and index < 16 and keys == 's'):
        print('Выход за границы')
    elif ((index % 4 == 0 or index == 0) and keys == 'a'):
        print('Выход за границы')
    elif ((index + 1) % 4 == 0 and keys == 'd'):
        print('Выход за границы')
    else:
         locat = fields.index('x')
         key = MOVES[keys]
         fields[locat], fields[locat + key] = fields[locat + key], fields[locat]
    return fields


def handle_user_input():
    moving = input('Введите значение:')
    if moving in MOVES or moving == 'cheat':
        return moving
    if moving in MOVES or moving == KeyboardInterrupt:
        return moving
    else:
        return False


def main():
    result_number = shuffle_field()
    print_field(result_number)
    while is_game_finished(result_number) == False:
        try:
            handle = handle_user_input()
            if handle and handle != 'END' and handle != 'cheat':
                result_number = perform_move(result_number, handle)
                print_field(result_number)
            elif handle == 'END':
                print('shutting down')
                break
            elif handle == 'cheat':
                cheat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']
            if(is_game_finished(cheat)):
                print('Вы воспользовались читом')
                print_field(cheat)
                break
            else:
                print('Неверные данные попробуйте еще раз:')
        except KeyboardInterrupt:
            print('shutting down')
            print('shutting down')
    while is_game_finished(result_number) == True:
        print('Поздравляем вы выиграли:')
        break


main()
