import re
 
pattern =r"^an"
 
string ="anfay"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')