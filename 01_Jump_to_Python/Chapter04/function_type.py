#coding: cp949
# 입력: 인자(Argument, Parameter)
# 출력: return (print 아님)
def my_sum1(num1, num2): #입력 O, 출력 O
    #연산, 비지니스 로직에만 집중
    result = num1 + num2
    return result

def my_sum2(num1, num2): #입력 O, 출력 X
    #출력이 필요없거나 모두 처리하고자 할때
    result = num1 + num2 
    print("%d+%d=%d"%(num1,num2,result))

def my_sum3(): #입력 X, 출력 O
    #함수 안에서 입력을 처리
    num1 = input("첫번째 수를 입력하세요: ")
    num2 = input("두번째 수를 입력하세요: ")
    result = num1 + num2 
    return result

def my_sum4(): #입력 X, 출력 X
    #함수안에서 모든 것을 처리
    num1 = input("첫번째 수를 입력하세요: ")
    num2 = input("두번째 수를 입력하세요: ")
    result = num1 + num2
    print("%d+%d=%d"%(num1,num2,result))

num1 = input("첫번째 수를 입력하세요: ")
num2 = input("두번째 수를 입력하세요: ")
result = my_sum1(num1, num2)
print("%d+%d=%d"%(num1,num2,result))

num1 = input("첫번째 수를 입력하세요: ")
num2 = input("두번째 수를 입력하세요: ")
my_sum2(num1, num2)

result = my_sum3()
print("%d+%d=%d"%(num1,num2,result))

my_sum4()
