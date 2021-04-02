import re


pattern = "a.y"
test_string = "baaabyys"
result = re.search(pattern, test_string)
print(f"Capture du caractère {result.start()} à {result.end()}")
print(f"Groupe capturé : {result.group()!r}")
