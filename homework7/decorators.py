
def cancel(func):
    def cancel_func():
        return IndexError(func.__name__,'is canceled!')
    return cancel_func


def count_execution(func):
    def wrapper():
        t1 = time.time()
        res = func()
        t2 = time.time()
        return (t2 - t1), res
    return wrapper


def catch(func):
    def wrapper():
        try:
            print(func())
        except Exception as e:
            print(e)

