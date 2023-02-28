import re

r = 'My grey cat ' \
         'Oh my gray flower'
res = re.findall(r'\bgrey\b', r)
print(res)

res = re.findall(r'gr[ea]y', r)
print(res)

r1 = 'separete seperete saperete separate'
res = re.findall(r's[ae]p[ae]r[ae]te', r1)
print(res)

r2 = 'Google google googlE goog'
res = re.findall(r'[Gg]oogle', r2)
print(res)

r3 = 'h1 h2 h3 h4 h5 h6 h7 a1 a2 a3 a4'
res = re.findall(r'h[0-4]', r3)
print(res)

r4 = 'sun cat'
res = re.findall(r'cat$', r4)
print(res)
r5 = 'cat sun'
res = re.findall(r'^cat', r5)
print(res)

res = re.findall(r'[ah][1-3]', r3)
print(res)

r6 = '1928.12.10 1999/12/01 2005:05:01 2000-01-01 1950-6-5'
res = re.findall(r'[12][0-9][0-9][0-9][./:-][0-1][0-9][./:-][0-3][0-9]', r6)
print(res)


