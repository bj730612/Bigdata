#coding: cp949

item=int(input('총건수 : '))
page_per_notice=int(input('한페이지 당 게시물수 : '))

total_page=item//page_per_notice
if item % page_per_notice != 0:
    total_page+=1
print(total_page)
