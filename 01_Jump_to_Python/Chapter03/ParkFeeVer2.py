#coding: cp949

age=int(input('나이를 입력하세요. : '))
if age >= 0 and age <= 3:
	fee='무료'
	print('요금은 %s 입니다.'%fee)
elif age >= 4 and age <= 13:
	fee=2000
	print('요금은 %d원 입니다.'%fee)
elif age >= 14 and age <= 18:
	fee=3000
	print('요금은 %d원 입니다.'%fee)
elif age >= 19 and age <= 65:
	fee=5000
	print('요금은 %d원 입니다.'%fee)
elif age >= 66:
	fee='무료'
	print('요금은 %s 입니다.'%fee)
elif age < 0:
	print("다시 입력하세요.")
