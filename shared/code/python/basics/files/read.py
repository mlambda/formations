with open("example.txt", encoding="utf8") as fh:
    print(fh.read())

with open("example.txt", encoding="utf8") as fh:
    for line in fh:
        print(line)

with open("example.txt", encoding="utf8") as fh:
    lines = fh.readlines()
    print(len(lines))
