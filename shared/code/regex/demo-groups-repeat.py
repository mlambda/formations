pattern = re.compile(r'(b.d)+')
r = pattern.finditer('abcdbzdbydbhdefgh')
for res in r:
  print(res.group(0),res.group(1),res.span())