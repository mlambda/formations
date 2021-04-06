def decorator(function):
    def new_function(*args, **kwargs):
        print("Avant l'appel de la fonction originale")
        result = function(*args, **kwargs)
        print("Après l'appel de la fonction originale")
        return result

    return new_function


@decorator
def add(a, b):
    return a + b
