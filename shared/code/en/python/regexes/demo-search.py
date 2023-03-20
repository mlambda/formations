import re

pattern = "a.y"
test_string = "baaabyys"
result = re.search(pattern, test_string)
print(f"Capture of characters {result.start()} to {result.end()}")
print(f"Captured group: {result.group()!r}")
