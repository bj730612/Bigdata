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
	print("�ٽ� �Է��ϼ���.")
money=int(input('����� �Է��ϼ���. : '))
if money < 0:
    print('�ٽ� �Է��ϼ���.')
else:
    if money > fee:
        print('�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�.' %(money-fee))
    elif money == fee:
        print('�����մϴ�. Ƽ���� �����մϴ�.')
    else:
        print('%d���� ���ڶ��ϴ�. �Է� �Ͻ� %d���� ��ȯ�մϴ�.' %(fee-money, money))
