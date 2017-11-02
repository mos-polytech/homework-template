from functools import reduce


def modulo_five():
    modulo_list = [1, 4, 5, 30, 99]
    modulo_five = list(map (lambda x: x % 5, modulo_list))
    return modulo_five


def to_string():
    to_string_list = [3, 4, 90, -2]
    to_string = list(map (lambda x: str(x), to_string_list))
    return to_string


def filter_string():
    filter_string_list = ['some', 1, 'v', 40, '3a', str]
    filter_string = list(filter (lambda x: type(x) != str, filter_string_list))
    return filter_string


def count_letters():
    count_letters_list = ['some', 'other', 'value']
    count_letters = reduce(lambda a, x: a + len(x), count_letters_list,0)
    return count_letters
