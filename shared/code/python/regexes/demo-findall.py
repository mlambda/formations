import re


pattern = "b.."
test_string = "baaabyys"
result = re.findall(pattern, test_string)
print(result)
