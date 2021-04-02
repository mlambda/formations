import re


pattern = "b.."
test_string = "baaabyys"
result = re.finditer(pattern, test_string)
for r in result:
    print(f"{r.group()!r} de l'indice {r.start()} à {r.end()}")
