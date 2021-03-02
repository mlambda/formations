import collections


Color = collections.namedtuple("Color", ["r", "g", "b"])
blue = Color(0, 0, 255)
print(blue.r, blue.g, blue.b)
