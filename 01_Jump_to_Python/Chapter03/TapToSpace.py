#coding: cp949

def code(c):
    for i in c:
        if i=="\t":
            c.replace(i,"    ")
        else:
            pass
    print(c)
    
code("탭\t을\t공백\t으로 바꾸는 프로그램")
