# -*- coding: utf-8 -*-

import random

import sys

EMPTY_MARK = 'x' #переменная с х
MOVES = { # задаем движение
'w' : -4,
's' : 4,
'a' :  -1,
'd' : 1,
}
def shuffle_field():
    number_for_games = [] #создаем массив
    for i in range(1,16):#включаем цикл от 1 до 16
        number_for_games.append(i) #добавляем  в конец массива
    number_for_games.append(EMPTY_MARK) # добавляем в конец
    random.shuffle(number_for_games) # перемешиваем значения
    return number_for_games #возвращаем значени
def print_field(number_for_games):
    j = 0 # задаем цикл
    while j<len(number_for_games): #Задаем цикл где J меньше массива numbers_for games
        print(number_for_games[j],number_for_games[j+1],number_for_games[j+2],number_for_games[j+3]) #Печатаем матрицу 4 на 4
        j+=4
def is_game_finished(number_for_games): #игра закончена
    # number_for_games.index('x')
    wins_checks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'x'] # выйгрышная комбинация
    if number_for_games == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'x'] : #  если массив равен выйграшной комбинации
        return  True # возвращаем тру
    elif number_for_games == wins_checks: # Если иначе равен
        return True
    else:
        return False
def perform_move(number_for_games,keys):
    move_key = MOVES[keys]
    index = number_for_games.index('x')
    if ((index >= 0 and index < 4 and keys == 'w') or ((index % 4 == 0 or index == 0) and keys == 'a')):
        print('Выход за  границы')
    elif  (index >= 12 and index < 16 and keys == 's') or((index + 1) % 4 == 0 and keys == 'd'):
        print('Выход за боковые границы')
    else:
         location = number_for_games.index('x')
         move_key = MOVES[keys]
         number_for_games[location], number_for_games[location + move_key] = number_for_games[location + move_key],number_for_games[location]
    return number_for_games
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
    while is_game_finished(result_number)==False:
        handle= handle_user_input()
        if handle and handle !='END' and handle != 'cheat':
            result_number = perform_move(result_number,handle)
            print_field(result_number)
        elif handle=='END':
            print('shutting down')
            break
        elif handle == 'cheat':
            cheat = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'x']
            if(is_game_finished(cheat)):
                print('Вы воспользовались читом')
                print_field(cheat)
                break
        else:
            print('Неверные данные попробуйте еще раз:')
    while is_game_finished(result_number)==True:
        print('Поздравляем вы выиграли:')
        break
main()