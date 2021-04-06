def double(limit):
    for i in range(limit):
        yield i * 2


total = 0
for i in double(1_000_000_000):
    total += i
print(total)
