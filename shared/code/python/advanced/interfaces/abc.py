import abc


class Model(abc.ABC):
    @abc.abstractmethod
    def compute(self, data: list[int]) -> float:
        raise NotImplementedError()


class Sum(Model):
    def compute(self, data: list[int]) -> float:
        return sum(data)
