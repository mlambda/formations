import contextlib


@contextlib.contextmanager
def MyContext():
    try:
        print("Entrée dans le contexte")
        yield
    finally:
        print("Sortie du contexte")


with MyContext():
    print("Corps du contexte")
