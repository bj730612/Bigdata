f = open('새파일.txt', 'r', encoding='utf-8')

data = f.read()

print(data)
f.close()