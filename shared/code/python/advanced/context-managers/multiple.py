with open("input.txt") as fh_r, open("output.txt", "w") as fh_w:
    for line in fh_r:
        fh_w.write(line * 2)
