pattern = re.compile(r'([a-zA-Z]+)(\d+)g*')
r = pattern.finditer('A361224g B4012_w44g')
for res in r:
  print(res.group(0), res.group(1), res.group(2))