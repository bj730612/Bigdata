#coding: cp949

coffee_number = 10

print("<SW 아키텍처 커피자판기 Ver1.0>")
menu="""
<Menu>
메뉴를 선택하세요
1. 커피구매
2. 커피잔량확인
3. 프로그램 종료
"""

while True:
    print(menu)
    menu_number = int(input("메뉴를 선택하세요: "))
    if menu_number == 1:
        money = int(input("금액을 입력하세요: "))
        if money == 300:
            print("커피를 줍니다\n.")
            coffee_number = coffee_number - 1
        elif money > 300:
            print("거스름돈 %d원을 주고 커피를 줍니다.\n" %(money-300))
            coffee_number = coffee_number - 1
        else:
            short_money = 300 - money
            print("금액이 %d원 모자랍니다.\n돈을 돌려주고 커피를 주지 않습니다." %short_money)
    if menu_number == 2:
        print("남은 커피의 양은 %d개입니다.\n" %coffee_number)
    if menu_number == 3:
        print("프로그램을 종료합니다.\n")
        break

