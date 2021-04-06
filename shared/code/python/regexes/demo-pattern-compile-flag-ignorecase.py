import re


test = "0ab12Ab3491019AB"
pattern = re.compile(r"\d+[ab]")
print(pattern.findall(test))
pattern = re.compile(r"\d+[ab]\D*", re.IGNORECASE)
print(pattern.findall(test))
