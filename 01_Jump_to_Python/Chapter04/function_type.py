#coding: cp949
# �Է�: ����(Argument, Parameter)
# ���: return (print �ƴ�)
def my_sum1(num1, num2): #�Է� O, ��� O
    #����, �����Ͻ� �������� ����
    result = num1 + num2
    return result

def my_sum2(num1, num2): #�Է� O, ��� X
    #����� �ʿ���ų� ��� ó���ϰ��� �Ҷ�
    result = num1 + num2 
    print("%d+%d=%d"%(num1,num2,result))

def my_sum3(): #�Է� X, ��� O
    #�Լ� �ȿ��� �Է��� ó��
    num1 = input("ù��° ���� �Է��ϼ���: ")
    num2 = input("�ι�° ���� �Է��ϼ���: ")
    result = num1 + num2 
    return result

def my_sum4(): #�Է� X, ��� X
    #�Լ��ȿ��� ��� ���� ó��
    num1 = input("ù��° ���� �Է��ϼ���: ")
    num2 = input("�ι�° ���� �Է��ϼ���: ")
    result = num1 + num2
    print("%d+%d=%d"%(num1,num2,result))

num1 = input("ù��° ���� �Է��ϼ���: ")
num2 = input("�ι�° ���� �Է��ϼ���: ")
result = my_sum1(num1, num2)
print("%d+%d=%d"%(num1,num2,result))

num1 = input("ù��° ���� �Է��ϼ���: ")
num2 = input("�ι�° ���� �Է��ϼ���: ")
my_sum2(num1, num2)

result = my_sum3()
print("%d+%d=%d"%(num1,num2,result))

my_sum4()
