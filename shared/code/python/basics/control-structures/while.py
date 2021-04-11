ok = False
while not ok:
    answer = input("Please enter y or n:")
    ok = answer in ["y", "n"]

print(answer)
