import re

p = re.compile('^hello\s\w')
dest_str = "hello my hello world! hello!"
m = p.match(dest_str)
print(m)
m = p.findall(dest_str)
print(m)

p = re.compile('hello\s\w')
dest_str = "hello my hello world! hello!"
m = p.match(dest_str)
print(m)
m = p.findall(dest_str)
print(m)
