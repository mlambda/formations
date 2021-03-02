import random


def multiple(n):
    def decorator(function):
        def new_function(*args, **kwargs):
            return [function(*args, **kwargs) for _ in range(n)]

        return new_function

    return decorator


@multiple(10)
def randint(a, b):
    return random.randint(1, 6)
