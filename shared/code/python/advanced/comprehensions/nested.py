# Compréhensions
nm = [n * m for n in range(4) if n % 2 == 0 for m in range(4) if m % 2 == 1]
mn = [n * m for m in range(4) if m % 2 == 1 for n in range(4) if n % 2 == 0]

# Boucles for
nm = []
for n in range(4):
    if n % 2 == 0:
        for m in range(4):
            if m % 2 == 1:
                nm.append(n * m)
mn = []
for m in range(4):
    if m % 2 == 1:
        for n in range(4):
            if n % 2 == 0:
                mn.append(n * m)

# nm = [0, 0, 2, 6]
# mn = [0, 2, 0, 6]
