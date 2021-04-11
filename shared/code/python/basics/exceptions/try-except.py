def div(a, b):
    try:
        return a / b
    except ArithmeticError:
        return None


print(div(4, 3))
print(div(4, 0))
