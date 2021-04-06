pattern = re.compile(r"\d+[ab]\D*")
for r in pattern.finditer("0ab12Azerty3491019B"):
  print(r.group())
  