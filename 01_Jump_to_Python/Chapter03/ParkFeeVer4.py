#coding: cp949

rate_fee='������ ����� %s����̸� ����� %d�� �Դϴ�.'

age=int(input('���̸� �Է��ϼ���. : '))
if age >= 0 and age <= 3:
	rate='����'
	fee=0
	print('������ ����� %s ����� ���� �Դϴ�.'%rate)
elif age >= 4 and age <= 13:
	rate='���'
	fee=2000
	print (rate_fee %(rate, fee))
elif age >= 14 and age <= 18:
	rate='û�ҳ�'
	fee=3000
	print (rate_fee %(rate, fee))
elif age >= 19 and age <= 65:
	rate='����'
	fee=5000
	print (rate_fee %(rate, fee))
elif age >= 66:
	rate='����'
	fee=0
	print('������ ����� %s ����� ���� �Դϴ�.'%rate)
elif age < 0:
	print('�ٽ� �Է��ϼ���.')
menu=int(input('��� ������ �����ϼ���. (1: ����, 2: �������� �ſ�ī��) : '))
if menu == 1:
	money=int(input('����� �Է��ϼ���. : '))
	if money > fee:
		print('�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�.' %(money-fee))
	elif money == fee:
		print('�����մϴ�. Ƽ���� �����մϴ�.')
	else:
		print('%d���� ���ڶ��ϴ�. �Է� �Ͻ� %d���� ��ȯ�մϴ�.' %(fee-money) %money)
elif menu == 2:
	if age >= 60 and age <= 65:
		fee=fee*0.9*0.95
		print('%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.' %fee)
	elif age >= 4 and age < 60:
		fee=fee*0.9
		print('%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.' %fee)
