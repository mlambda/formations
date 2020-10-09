pattern = "b.."
test_string = 'baaabyys'
result = re.finditer(pattern, test_string)
for r in result:
  print(r.group()," index : [",
        r.start(),",",r.end(),"]")