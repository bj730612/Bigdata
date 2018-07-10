import csv
import math

def get_csv_row_instance(primary_key):
    row_instance=[]
    row_index = data[0].index(primary_key)

    for col in data[1:]:
        row_instance.append(col[row_index])

    return row_instance

def get_csv_col_instance(col_name):
    col_instance = []
    col_index = data[0].index(col_name)

    for row in data[1:]:
        col_instance.append(row[col_index])
    return col_instance

def Convert_Type(col_instance):
    try:
        col_instance = list(map(int, col_instance))
    except ValueError:
        col_instance = list(map(float, col_instance))
    return col_instance

def My_Sum(data_list):
    My_Sum=0
    col_instance=Convert_Type(get_csv_col_instance(data_list))
    for num in col_instance:
        My_Sum += num
        print(num)
    return My_Sum

def My_Average(data_list):
    My_Sum = 0
    My_Average = 0
    count = 0
    col_instance = Convert_Type(get_csv_col_instance(data_list))
    for num in col_instance:
        My_Sum += num
        count += 1
        My_Average = My_Sum / count
    return My_Average

def My_Max(data_list):
    My_Max = 0
    col_instance = Convert_Type(get_csv_col_instance(data_list))
    for num in col_instance:
        print(num)
        if My_Max < num:
            My_Max = num
    return My_Max

def My_Min(data_list):
    My_Min = get_csv_col_instance(data_list)[1]
    col_instance = Convert_Type(get_csv_col_instance(data_list))
    for num in col_instance:
        print(num)
        if My_Min > (num):
            My_Min = (num)
    return My_Min

def My_Deviation(data_list):
    My_Deviation=0
    col_instance = Convert_Type(get_csv_col_instance(data_list))
    print("편차(Deviation)공식 : 표본값 - 평균\n표본 편차")
    for num in col_instance:
        My_Deviation = num - My_Average(data_list)
        print(num + " " + My_Deviation)
    return My_Deviation

def My_Standard_Deviation(data_list):# 표준편차
    Variance=0
    # 내용을 작성하세요.
    return My_Standard_Deviation

def My_Variance(data_list):#분산
    My_Variance=0
    # 내용을 작성하세요.
    return My_Variance

def My_Ascendant(data_list):#오름차순
    # 내용을 작성하세요.
    pass

def My_Descendant(data_list):#내림차순
    # 내용을 작성하세요.
    pass

def print_row(row_instance):
    for row_element in row_instance:
        print("%s "%row_element, end='')
    pass

def print_col(col_instance):
    for row_element in col_instance:
        print(row_element)

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data=list(csv.reader(infile))


while True:
    print("<CSVHandle연습예제>\n0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬\n")
    menu = int(input("메뉴를 선택하세요: "))
    if menu == 0:
        print("프로그램을 종료합니다.")
        break
    elif menu == 1:
        primary_key = int(input("Access Key를 입력하세요.: "))
        print_row(data[primary_key])
        print()
    elif menu == 2:
        col_name = input("Access Key를 입력하세요.: ")
        print_col(get_csv_col_instance(col_name))
    elif menu == 3:
        data_list = input("Access Key를 입력하세요.: ")
        My_Sum(data_list)
        print(My_Sum(data_list))
    elif menu == 4:
        data_list = input("Access Key를 입력하세요.: ")
        My_Average(data_list)
        print_col(get_csv_col_instance(data_list))
        print(My_Average(data_list))
    elif menu == 5:
        data_list = input("Access Key를 입력하세요.: ")
        My_Max(data_list)
        print(My_Max(data_list))
    elif menu == 6:
        data_list = input("Access Key를 입력하세요.: ")
        My_Min(data_list)
        print(My_Min(data_list))
    elif menu == 7:
        data_list = input("Access Key를 입력하세요.: ")
        print_col(get_csv_col_instance(data_list))
        My_Deviation(data_list)
    pass