import pathlib


home = pathlib.Path.home()
print([str(p) for p in home.glob("**/*.jpg")])
