# f=open('새파일.txt','w',encoding='utf-8')
# f=open('./새파일.txt','w',encoding='utf-8')
# f=open('./temp/새파일.txt','w',encoding='utf-8')
# f=open('./temp/catagory/새파일.txt','w',encoding='utf-8')
f=open('.../temp/새파일.txt','w',encoding='utf-8')

for i in range(1,11):
    data = "%d번째 줄입니다.\n"%i

    f.write(data)

f.close()