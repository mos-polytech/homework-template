import pytest


def test_cancel(capsys):
    from homework7.decorators import cancel

    @cancel
    def some():
        print('done!')

    @cancel
    def other():
        print('done!')

    some()
    out, _ = capsys.readouterr()
    assert out == 'some is canceled!\n'

    other()
    out, _ = capsys.readouterr()
    assert out == 'other is canceled!\n'


def test_count_execution(capsys):
    from homework7.decorators import count_execution

    @count_execution
    def some(value):
        return value

    @count_execution
    def other():
        return 5

    for i in range(10):
        result = some(i)
        assert result == i

        out, _ = capsys.readouterr()
        assert out == str(i + 1) + '\n'

    result = other()
    assert result == 5

    out, _ = capsys.readouterr()
    assert out == '1\n'


def test_catch_broken():
    from homework7.decorators import catch

    message = 'Should not be captured'

    @catch
    def broken():
        raise KeyboardInterrupt(message)

    with pytest.raises(KeyboardInterrupt, message=message):
        broken()


def test_capture_safe():
    from homework7.decorators import catch

    @catch
    def safe(x, y):
        return x + y

    assert safe(1, 2) == 3


def test_catch_normal(capsys):
    from homework7.decorators import catch

    @catch
    def normal(text):
        raise ValueError(text)

    message = 'test'
    normal(message)
    out, _ = capsys.readouterr()
    assert out == message + '\n'
