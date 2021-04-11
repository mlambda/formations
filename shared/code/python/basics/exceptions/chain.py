class MathException(Exception):
    pass


try:
    1 / 0
except ArithmeticError as e:
    raise MathException("Division impossible") from e
