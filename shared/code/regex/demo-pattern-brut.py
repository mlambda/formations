pattern_lit  =  "\\\\"
pattern_brut = r"\\"
test_lit  =  "chaine\nono"
test_brut = r"chaine\nono"
for pattern in [pattern_lit,pattern_brut]:
  for test in [test_lit, test_brut]:
    if re.search(pattern, test) :
      print("capturé")
    else: 
      print("manqué")