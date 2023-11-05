table = [1, 8, 3, 4]
index = 0
maximum = table[index]
while index < len(table):
    if maximum < table[index]:
        maximum = table[index]
    index = index + 1
print(maximum)
