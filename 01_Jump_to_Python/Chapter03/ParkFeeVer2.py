#coding: cp949

age=int(input('���̸� �Է��ϼ���. : '))
if age >= 0 and age <= 3:
	fee='����'
	print('����� %s �Դϴ�.'%fee)
elif age >= 4 and age <= 13:
	fee=2000
	print('����� %d�� �Դϴ�.'%fee)
elif age >= 14 and age <= 18:
	fee=3000
	print('����� %d�� �Դϴ�.'%fee)
elif age >= 19 and age <= 65:
	fee=5000
	print('����� %d�� �Դϴ�.'%fee)
elif age >= 66:
	fee='����'
	print('����� %s �Դϴ�.'%fee)
elif age < 0:
	print("�ٽ� �Է��ϼ���.")
