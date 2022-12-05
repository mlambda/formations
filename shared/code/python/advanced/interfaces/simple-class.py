class Model:
    def compute(self, data: list[int]) -> float:
        raise NotImplementedError()


class Sum(Model):
    def compute(self, data: list[int]) -> float:
        return sum(data)
