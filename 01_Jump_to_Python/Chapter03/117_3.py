#coding: cp949
money = int(input("얼마를 가지고 있습니까? "))
card = input("카드를 소유하고 있습니까? (y/n) : ")
if card == 'y':     card = True
else:               card = False

if money >= 3000:
    print("택시를 타고 가라")
elif card == True:
#   print("택시를 타고 가라") # 동일한 코드일 경우 중복
    print("카드 지원택시]택시를 타고 가라") # 중복 코드 아닌경우 허용
else:
    print("걸어가라")
