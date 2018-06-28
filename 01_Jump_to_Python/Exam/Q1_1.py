

while(True):

    age = input("나이를 입력하세요 : ")

    if age == "종료":
        print("종료")
        break
    elif int(age) < 3:
        price = "무료"
        print("영화 입장권의 가격은", price)
    elif int(age) <= 12:
        price = 10
        print("영화 입장권의 가격은", price)
    elif int(age) >= 13:
        price = 15
        print("영화 입장권의 가격은", price)
