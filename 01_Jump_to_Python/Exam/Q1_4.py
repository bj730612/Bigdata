numbers = input("세개의 양수를 입력하세요 (종료-1): ")

numbers = numbers.split()

result = int(numbers[2])
num1 = int(numbers[0])
num2 = int(numbers[1])

if result % num1 == 0 and result % num2 == 0:
    print("%s는 %s와 %s의 공배수 입니다." % (result, num1, num2))
else:
    print("%s는 %s와 %s의 공배수가 아닙니다." % (result, num1, num2))