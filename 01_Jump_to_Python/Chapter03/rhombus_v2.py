#coding: cp949

while True:
    i, j= 0, 0
    base=(int)(input("Ȧ���� �Է��ϼ���.(0 <- ����): "))
    num=(base+1)/2
    if base%2 == 1:
        while num > i:
            print(" "*(int)(num-1-i),end="")
            print("*"*(int)((2*i)+1))
            i+=1
        while num > j+1 and j+1 < num:
            print(" "*(int)(j+1),end="")
            print("*"*(int)(base-(2*(j+1))))
            j+=1
    elif base == 0:
        break
    else:
        print("¦���� �Է��ϼ̽��ϴ�. �ٽ� �Է��ϼ���")
