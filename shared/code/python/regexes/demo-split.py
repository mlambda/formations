import re


test = "J'aime les expressions régulières"
p = re.compile(r"\W+")
print(p.split(test))
maxsplit = 2
print(p.split(test, maxsplit))
