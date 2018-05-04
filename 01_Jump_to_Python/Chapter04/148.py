#coding: cp949

def cal(choice, *args):
    if choice == 'sum':
        result = args[0]
        for i in args[1:]:
            result += i
    elif choice == 'sub':
        result = args[0]
        for i in args[1:]:
            result -= i
    elif choice == 'mul':
        result = args[0]
        for i in args[1:]:
            result *= i
    elif choice == 'div':
        result = args[0]
        for i in args[1:]:
            result /= i
    return result
result = cal('sum', 1,2,3)
print(result)
result = cal('sub', 1,2,3)
print(result)
result = cal('mul', 1,2,3)
print(result)
result = cal('div', 1,2,3)
print(result)

