import collections


chainmap = collections.ChainMap(dict(a=1), dict(a=2, b=3))
print(chainmap["a"], chainmap["b"])
