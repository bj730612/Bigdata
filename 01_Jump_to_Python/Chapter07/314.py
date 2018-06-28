import re

p = re.compile('Crow|Servo')
m = p.match('Crow')
print(m)
m = p.match('Servo')
print(m)
m = p.match('My keyword is Servo')
print(m)
m = p.search('My keyword is Servo')
print(m)

p = re.compile('short$')
m = p.search('short man is strong')
print(m)
m = p.search('life is like short journey')
print(m)
m = p.search('Life is too short')
print(m)
