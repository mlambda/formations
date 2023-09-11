tableau = [1, 8, 3, 4]
index = 0
maximum = tableau[index]
while index < len(tableau):
    if maximum < tableau[index]:
        maximum = tableau[index]
    index = index + 1
print(maximum)
