from functools import reduce


def modulo_five():
    return list(map(lambda x: x % 5, [1, 4, 5, 30, 99]))


def to_string():
    return list(map(lambda x: str(x), [3, 4, 90, -2]))


def filter_string():
    return list(filter(lambda x: type(x) != str, ['some', 1, 'v', 40, '3a', str]))


def count_letters():
    return reduce(lambda a, x: a + len(x), ['some', 'other', 'value'],0)
