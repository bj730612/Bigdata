#coding: cp949

item=int(input('�ѰǼ� : '))
page_per_notice=int(input('�������� �� �Խù��� : '))

total_page=item//page_per_notice
if item % page_per_notice != 0:
    total_page+=1
print(total_page)
