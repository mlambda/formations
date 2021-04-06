total = 0
generator = (n ** 2 for n in range(1_000_000_000))
for i in generator:
    total += i
print(total)
