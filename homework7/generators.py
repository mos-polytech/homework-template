import random
from datetime import datetime, timedelta


def all_even_numbers():
    list = [x for x in range(0, 101, 2)]
    yield list


def random_increasing_number():
    number = 1
    while True:
        yield number
        some = int(random.uniform(0, 100))
        number = number + some


def next_day():
    today = datetime.today().date()
    for i in range(100):
        yield today
        today += timedelta(days=1)

