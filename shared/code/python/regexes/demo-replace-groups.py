import re


test = '{"first_name":"James","last_name":"Bond"}'
p = re.compile(r'^\{"(\S+)":"(\S+)","(\S+)":"(\S+)"\}$')
print(p.sub(r"Person(\1='\2', \3='\4')", test))
