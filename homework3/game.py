import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x', ]
    random.shuffle(field)
    return(field)


def print_field(field):
    line = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            line[j] = field[i * 4 + j]
        print(line)


def is_game_finished(field):
    if field == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x', ]:
        return(True)
    else:
        return(False)


def perform_move(field, key):
    index = 0

    for i in range(len(field)):
        if field[i] == EMPTY_MARK:
            index = i
    if (index + key >= 0) and (index + key < 16):
        if (key == 1 or key == -1) and \
                (((index + key) % 4 == 0) and ((index % 4 == 3))) \
                or (((index + key) % 4 == 3) and ((index % 4 == 0))):
            print('Вы не можете так ходить!')
            return (field)
        else:
            field[index], field[index + key] = field[index + key], field[index]
            return (field)
    else:
        return (False)


def handle_user_input():
    user_decision = input('Управляйте игрой с помощью W,A,S и D. Ваш ход: ')
    while user_decision not in MOVES:
        print('Ошибка!')
        user_decision = input('Управляйте игрой с помощью W,A,S и D. Ваш ход: ')
    else:
        return(MOVES[user_decision])


def main():
    print('Начало игры!')
    first_field = shuffle_field()
    print_field(first_field)
    count = 0
    while not(is_game_finished(first_field)):
        key = handle_user_input()
        nwe_one_field = (perform_move(first_field, key))
        if nwe_one_field is False:
            print('Вы не можете так ходить!')
        else:
            first_field = nwe_one_field
            print_field(first_field)
            count += 1
    print('Поздравляем! ВЫ ВЫИГРАЛИ! Количество ходов :', count)

if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
