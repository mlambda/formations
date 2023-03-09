with open("example.txt", mode="w", encoding="utf8") as fh:
    fh.write("My text\n")

with open("example.txt", mode="w", encoding="utf8") as fh:
    fh.writelines(["My first line\n", "My second line\n"])
