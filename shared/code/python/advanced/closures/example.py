def make_average() -> Callable[[float], float]:
    total = 0
    n = 0

    def average(x: float) -> float:
        nonlocal total, n
        total += x
        n += 1
        return total / n

    return average


avg = make_average()
print(avg(2))
print(avg(3))
