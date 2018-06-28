import re

p = re.compile('[a-z]+')
m = p.match("python")
print(m)
m = p.match("3 python")
print(m)
m = p.match("python ver3.6")
print(m)

m = p.search("python")
print(m)
m = p.search("3 python")
print(m)

m = p.match("life is too short")
print(m)
m = p.search("life is too short")
print(m)
m = p.findall("life is too short")
print(m)

result = p.finditer("life is too short")
for r in result:
    print(r)
