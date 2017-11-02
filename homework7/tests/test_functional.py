import inspect


def test_modulo_five():
    from homework7.functional import modulo_five
    lines = inspect.getsource(modulo_five)

    assert 'map(' in lines
    assert modulo_five() == [1, 4, 0, 0]


def test_to_string():
    from homework7.functional import to_string
    lines = inspect.getsource(to_string)

    assert 'map(' in lines
    assert to_string() == ['3', '4', '90', '-2']


def test_filter_string():
    from homework7.functional import filter_string
    lines = inspect.getsource(filter_string)

    assert 'filter(' in lines
    assert filter_string() == [1, 40, str]


def test_count_letters():
    from homework7.functional import count_letters
    lines = inspect.getsource(count_letters)

    assert 'reduce(' in lines
    assert count_letters() == 14
