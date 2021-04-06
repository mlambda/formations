import contextlib


@contextlib.contextmanager
def MyContext():
    try:
        print("Entrée dans le contexte")
        yield "Valeur retournée"
    finally:
        print("Sortie du contexte")


with MyContext() as value:
    print(value)
    print("Corps du contexte")
