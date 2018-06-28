import re

p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$')
m = p.match('foo.bar')
print(m)
m = p.match('autoexec.bat')
print(m)
m = p.match('sendmail.cf')
print(m)

p = re.compile('.*[.](?!bat$).*$')
m = p.match('foo.bar')
print(m)
m = p.match('autoexec.bat')
print(m)
m = p.match('sendmail.cf')
print(m)
