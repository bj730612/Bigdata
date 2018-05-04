#coding: cp949

rate_fee='귀하의 등급은 %s등급이며 요금은 %d원 입니다.'
free_ticket=3
discount_ticket=5
count=0

while True:
	age=int(input('나이를 입력하세요. : '))
	if age >= 0 and age <= 3:
		rate='유아'
		fee=0
		print('귀하의 등급은 %s 요금은 무료 입니다.'%rate)
		continue
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
		continue
	elif age < 0:
		print('다시 입력하세요.')
		continue
	menu=int(input('요금 유형을 선택하세요. (1: 현금, 2: 공원전용 신용카드) : '))
	if menu == 1:
		money=int(input('요금을 입력하세요. : '))
		if money > fee:
			print('감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.' %(money-fee))
			count+=1
			if count % 7 == 0 and free_ticket != 0:
				free_ticket-=1
				print('축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장' %free_ticket)
			elif count % 4 == 0 and discount_ticket != 0:
				discount_ticket-=1
				print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" %discount_ticket)
		elif money == fee:
			print('감사합니다. 티켓을 발행합니다.')
			count+=1
			if count % 7 == 0 and free_ticket != 0:
				free_ticket-=1
				print('축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장' %free_ticket)
			elif count % 4 == 0 and discount_ticket != 0:
				discount_ticket-=1
				print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" %discount_ticket)
		else:
			print('%d원이 모자랍니다. 입력 하신 %d원을 반환합니다.' %(fee-money) %money)
	elif menu == 2:
		if age >= 60 and age <= 65:
			fee=fee*0.9*0.95
			print('%d원 결제 되었습니다. 티켓을 발행합니다.' %fee)
			count+=1
			if count % 7 == 0 and free_ticket != 0:
				free_ticket-=1
				print('축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장' %free_ticket)
			elif count % 4 == 0 and discount_ticket != 0:
				discount_ticket-=1
				print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" %discount_ticket)
		elif age >= 4 and age < 60:
			fee=fee*0.9
			print('%d원 결제 되었습니다. 티켓을 발행합니다.' %fee)
			count+=1
			if count % 7 == 0 and free_ticket != 0:
				free_ticket-=1
				print('축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장' %free_ticket)
			elif count % 4 == 0 and discount_ticket != 0:
				discount_ticket-=1
				print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" %discount_ticket)
