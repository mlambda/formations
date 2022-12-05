import abc


class Data(abc.ABC):
    pass


Data.register(list)

assert issubclass(list, Data)
assert isinstance((), Data)
