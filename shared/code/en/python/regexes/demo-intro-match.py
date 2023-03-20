import re

patterns = ["a.*s", "^b", "s$", "a+b", "a{4,5}b", "y*b"]
test_string = "baaabyys"
for pattern in patterns:
    if re.match(pattern, test_string):
        print(f"{pattern:10} matched")
    else:
        print(f"{pattern:10} did not match")
