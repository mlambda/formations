with open("example.txt", mode="w", encoding="utf8") as fh:
    fh.write("Mon texte\n")

with open("example.txt", mode="w", encoding="utf8") as fh:
    fh.writelines(["Ma première ligne\n", "Ma deuxième ligne\n"])
