f = open('새파일.txt','r', encoding='utf-8')
while True:
    line = f.readline()
    if not line:
        break
    print(line,end='')
f.close()