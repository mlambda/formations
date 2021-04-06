import re


p = re.compile("(blue|red|green)")
print(p.sub("colour", "blue socks and red shoes"))
print(p.sub("colour", "blue socks and red shoes", count=1))
