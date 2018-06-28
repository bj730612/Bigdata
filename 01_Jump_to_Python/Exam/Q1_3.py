
while(True):
    number = input("양수를 입력하세요 (종료-1): ")
    if number == "-1":
        print("종료")
        break
    elif int(number) % 10 == 0:
        print("true")
    else:
        print("false")