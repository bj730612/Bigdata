#coding: cp949

rate_fee='귀하의 등급은 %s등급이며 요금은 %d원 입니다.'

age=int(input('나이를 입력하세요. : '))
if age >= 0 and age <= 3:
	rate='유아'
	fee=0
	print('귀하의 등급은 %s 요금은 무료 입니다.'%rate)
elif age >= 4 and age <= 13:
	rate='어린이'
	fee=2000
	print (rate_fee %(rate, fee))
elif age >= 14 and age <= 18:
	rate='청소년'
	fee=3000
	print (rate_fee %(rate, fee))
elif age >= 19 and age <= 65:
	rate='성인'
	fee=5000
	print (rate_fee %(rate, fee))
elif age >= 66:
	rate='노인'
	fee=0
	print('귀하의 등급은 %s 요금은 무료 입니다.'%rate)
elif age < 0:
	print('다시 입력하세요.')
menu=int(input('요금 유형을 선택하세요. (1: 현금, 2: 공원전용 신용카드) : '))
if menu == 1:
	money=int(input('요금을 입력하세요. : '))
	if money > fee:
		print('감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.' %(money-fee))
	elif money == fee:
		print('감사합니다. 티켓을 발행합니다.')
	else:
		print('%d원이 모자랍니다. 입력 하신 %d원을 반환합니다.' %(fee-money) %money)
elif menu == 2:
	if age >= 60 and age <= 65:
		fee=fee*0.9*0.95
		print('%d원 결제 되었습니다. 티켓을 발행합니다.' %fee)
	elif age >= 4 and age < 60:
		fee=fee*0.9
		print('%d원 결제 되었습니다. 티켓을 발행합니다.' %fee)
