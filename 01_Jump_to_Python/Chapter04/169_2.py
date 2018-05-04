count=0

f = open("sample.txt")
lines = f.readlines()
f.close()

total=0
for line in lines:
    score = int(line)
    total += score

average = total/len(lines)

f = open('result.txt','w',encoding='utf-8')
f.write(str(average))
f.close()