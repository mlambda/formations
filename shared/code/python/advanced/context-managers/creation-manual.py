class MyContext:
    def __enter__(self):
        print("Entrée dans le contexte")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Sortie du contexte")
        return False


with MyContext():
    print("Corps du contexte")
