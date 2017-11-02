import datetime
import random
import types


def test_even_numbers():
    from homework7.generators import all_even_numbers

    assert isinstance(all_even_numbers(), types.GeneratorType)
    assert list(all_even_numbers()) == list(range(0, 100, 2))


def test_numbers_are_random():
    from homework7.generators import random_increasing_number

    g1 = random_increasing_number()
    random.seed(1)
    test1 = [next(g1) for _ in range(10)]

    g2 = random_increasing_number()
    random.seed(2)
    test2 = [next(g2) for _ in range(10)]

    assert test1 != test2


def test_numbers_are_increasing():
    from homework7.generators import random_increasing_number

    g = random_increasing_number()
    seq = [next(g) for _ in range(100)]
    assert all(earlier <= later for earlier, later in zip(seq, seq[1:]))


def test_next_day():
    from homework7.generators import next_day

    g = next_day()
    today = datetime.datetime.today().date()

    for i in range(100):
        assert next(g) == today + datetime.timedelta(days=i)
