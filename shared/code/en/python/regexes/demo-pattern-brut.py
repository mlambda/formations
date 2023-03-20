import re

pattern_raw = "\\\\"
pattern_normal = r"\\"
test_normal = "before\nafter"
test_raw = r"before\nafter"
for pattern in [pattern_normal, pattern_raw]:
    for test in [test_normal, test_raw]:
        if re.search(pattern, test):
            print("matched")
        else:
            print("did not match")
