with open("example.txt", encoding="utf8") as fh_read, open(
    "example-upper.txt", mode="w", encoding="utf8"
) as fh_write:
    fh_write.write(fh_read.read().upper())
