import re


test = "Élève très studieux"
pattern = re.compile(r"\w+")
print(pattern.findall(test))
pattern = re.compile(r"\w+", re.ASCII)
print(pattern.findall(test))
