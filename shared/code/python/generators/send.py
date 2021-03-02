def squares():
    while True:
        value = (yield) ** 2
        print(value)


generator = squares()
next(generator)
for i in range(10):
    generator.send(i)
