#coding: cp949

def code(c):
    for i in c:
        if i=="\t":
            c.replace(i,"    ")
        else:
            pass
    print(c)
    
code("��\t��\t����\t���� �ٲٴ� ���α׷�")
