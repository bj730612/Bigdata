#coding: cp949

coffee_number = 10

print("<SW ��Ű��ó Ŀ�����Ǳ� Ver1.0>")
menu="""
<Menu>
�޴��� �����ϼ���
1. Ŀ�Ǳ���
2. Ŀ���ܷ�Ȯ��
3. ���α׷� ����
"""

while True:
    print(menu)
    menu_number = int(input("�޴��� �����ϼ���: "))
    if menu_number == 1:
        money = int(input("�ݾ��� �Է��ϼ���: "))
        if money == 300:
            print("Ŀ�Ǹ� �ݴϴ�\n.")
            coffee_number = coffee_number - 1
        elif money > 300:
            print("�Ž����� %d���� �ְ� Ŀ�Ǹ� �ݴϴ�.\n" %(money-300))
            coffee_number = coffee_number - 1
        else:
            short_money = 300 - money
            print("�ݾ��� %d�� ���ڶ��ϴ�.\n���� �����ְ� Ŀ�Ǹ� ���� �ʽ��ϴ�." %short_money)
    if menu_number == 2:
        print("���� Ŀ���� ���� %d���Դϴ�.\n" %coffee_number)
    if menu_number == 3:
        print("���α׷��� �����մϴ�.\n")
        break

