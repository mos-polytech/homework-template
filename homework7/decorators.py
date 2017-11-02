def cancel(func):
    def cancel_func():
        return IndexError(func.__name__, 'is canceled!')
    return cancel_func


def count_execution(func):
    pass


def catch(func):
    def wrapper():
        try:
            print(func())
        except Exception as e:
            print(e)
