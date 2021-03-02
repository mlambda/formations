def integers(n):
    for i in range(n):
        yield i


def integers_repeated(n, repeat_n):
    for i in range(repeat_n):
        yield from integers(n)


for i in integers_repeated(3, 2):
    print(i)
