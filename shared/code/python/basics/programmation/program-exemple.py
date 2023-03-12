X = [1, 8, 3, 4]
index = 0
Y = X[index]
while index < len(X):
    if Y < X[index]:
        Y = X[index]
    index = index + 1
print(Y)
