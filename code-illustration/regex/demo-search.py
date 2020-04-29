import re
pattern = "a.y"
test_string = 'baaabyys'
result = re.search(pattern, test_string)
print("Capturé depuis le caractère",result.start(),
      "à",result.end())
print("Groupe capturé : ",result.group())
