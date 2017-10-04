# coding: utf-8
# In[ ]:
# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
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
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    # generate solved field field
    field = [i for i in range(1, 16)]
    field.append(EMPTY_MARK)

    allowed_moves = list(MOVES.keys())
    # messed up it
    for i in range(1000):
        try:
            # emulate allowed random moves, so it's always be solvable
            rand_key = allowed_moves[random.randint(0, len(allowed_moves) - 1)]
            field = perform_move(field, rand_key)
        except IndexError:
            pass

    return field

def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    n = 4
    print('------------------------')
    for i in range(0, len(field), n):
        prepared_line = ['{:2s}'.format(str(x)) for x in field[i:i + n]]
        print(prepared_line)
    print('------------------------')

def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    for i in range(1, len(field) - 1):
        if field[i] == EMPTY_MARK or field[i - 1] == EMPTY_MARK:
            return False
        if field[i - 1] > field[i]:
            return False
    return True

def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    mark_position = field.index(EMPTY_MARK)
    next_mark_position = mark_position + MOVES[key]
    if not (0 < next_mark_position < len(field)):
        raise IndexError()
    # left move restrictions
    if mark_position in [0, 4, 8, 12] and key == 'a':
        raise IndexError()
    # right move restrictions
    if mark_position in [3, 7, 11, 15] and key == 'd':
        raise IndexError()
    field_new = list(field)
    field_new[mark_position], field_new[next_mark_position] =        field_new[next_mark_position], field_new[mark_position]
    return field_new

def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move.
    """
    allowed_moves = list(MOVES.keys())
    move = ''
    while move not in allowed_moves:
        move = input('Next move (use wasd for control) \n')
    return move

def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    counter = 0
    while not is_game_finished(field):
        print_field(field)
        move = handle_user_input()
        try:
            field = perform_move(field, move)
            counter += 1
        except IndexError:
            print('It is impossible move')
    print('Nice one, you win!')
    print('Number of moves you make: ', counter)
    print_field(field)

if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    try:
        main()
    except KeyboardInterrupt:
        print('shutting down')

# In[ ]: