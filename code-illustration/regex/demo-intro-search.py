import re
patterns = ['a.*s', '^b', 's$', 'a+b', 'a{4,5}b','y*b']
test_string = 'baaabyys'
for pattern in patterns:
    if re.search(pattern, test_string):
        print("capturé","\t",pattern)
    else:
        print("manqué ","\t",pattern)
