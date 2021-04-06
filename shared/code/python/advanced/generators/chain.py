def squares(iterator):
    for item in iterator:
        yield item ** 2


def odd(iterator):
    for item in iterator:
        if item % 2:
            yield item


for i in squares(odd(range(10))):
    print(i)
