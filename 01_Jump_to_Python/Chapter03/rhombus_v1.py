#coding: cp949

while True:
    i = 0
    base=(int)(input("Ȧ���� �Է��ϼ���.(0 <- ����): "))
    num=(base+1)/2
    if base%2 == 1:
        while True:
            if num > i:
                print(" "*(int)(num-1-i),end="")
                print("*"*(int)((2*i)+1))
                i+=1
                if num <= i:
                    break
    elif base == 0:
        break
    else:
        print("¦���� �Է��ϼ̽��ϴ�. �ٽ� �Է��ϼ���")

