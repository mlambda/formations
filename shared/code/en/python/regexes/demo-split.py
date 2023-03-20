import re

test = "I love, regular. expressions"
p = re.compile(r"\W+")
print(p.split(test))
