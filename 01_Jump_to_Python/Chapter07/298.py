import re
p = re.compile('[abc]')
m = p.match("a")
print(m)
m = p.match("before")
print(m)
m = p.match("dude")
print(m)
m = p.match("dad")
print(m)

p = re.compile('[abc][abc]')
m = p.match("dad")
print(m)

p = re.compile('d[abc]')
m = p.match("dad")
print(m)

p = re.compile('[a-zA-Z]')
m = p.match("Zoo")
print(m)

p = re.compile('h[ijk]')
m = p.match("hi")
print(m)

p = re.compile('h[def]l[abc]o')
m = p.match("hello")
print(m)