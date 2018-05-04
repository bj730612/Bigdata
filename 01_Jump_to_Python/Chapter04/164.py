f = open('새파일.txt', 'r', encoding='utf-8')

lines = f.readlines()

for line in lines:
    print(line)

f.close()