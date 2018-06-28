import re

p = re.compile('ca{2}t')
m = p.match("cat")
print(m)
m = p.match("caat")
print(m)

p = re.compile('ca{2,5}t')
m = p.match("cat")
print(m)
m = p.match("caat")
print(m)
m = p.match("caaaaat")
print(m)

p = re.compile('ab?c')
m = p.match("ac")
print(m)
m = p.match("abc")
print(m)

p = re.compile('goo+gle')
m = p.match("gooooooooooooooooogle")
print(m)
m = p.match("gogle")
print(m)