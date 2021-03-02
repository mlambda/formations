def add(a, b):
    return a + b


add = timeit(multiple(10)(add))
