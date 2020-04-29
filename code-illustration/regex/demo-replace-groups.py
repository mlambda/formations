test = "id1234 : 'toto'  ; 23 "
p = re.compile(r'^.* :\s*(\S+)\s*;\s*(\S+)\s*.*$')
print(p.sub('myNewObject(\\1,\\2);', test))
