input_number = input("숫자열을 입력하세요 : ")

numbers = sorted(''.join(input_number))
for num in numbers:
    result = [''.join(numbers)]

if result == ["0123456789"]:
    print("true")
else:
    print("false")
