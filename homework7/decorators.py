
def cancel(func):
    def cancel_func():
        return IndexError(func.__name__,'is canceled!')
    return cancel_func


def count_execution(func):
    import time

    def wrappers():
        t = time.clock()
        return func.__name__, time.clock() - t
        yield wrappers
    def wrapper():
        wrapper.called += 1
        return func()

    wrapper.called = 0
    wrapper.__name__ = func.__name__
    return wrapper


def catch(func):
    def wrapper():
        try:
            print(func())
        except Exception as e:
            print(e)
