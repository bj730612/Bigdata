import glob
import json

g_json_bigdata = []
overlap_name = []

count = 0
learning_course_info_list = []

def create_student_id():
    with open('ITT_Student_id.txt', 'r', encoding='UTF-8') as f:
        id = f.read()
        id = id.split()


def get_learning_course_info_list():
    temp_learning_course_list = []
    if input("현재 수강 과목이 있습니까? (예: y/n) ") == "y":
        while True:
            temp_learning_course = {
                "course_code": input("강의코드 (예: IB171106, OB0104 ..): "),
                "course_name": input("강의명 (예: IOT 빅데이터 실무반): "),
                "teacher": input("강사 (예: 이현구): "),
                "open_date": input("개강일 (예: 2017-11-06): "),
                "close_date": input("종료일 (예: 2018-09-05): ")
            }
            temp_learning_course_list.append(temp_learning_course)

            if input("현재 수강하는 과목이 더 있습니까? (y/n) ") == 'n':
                break

    return temp_learning_course_list


def create_student_info():
    g_json_bigdata.append(
        {
            "address": input("주소를 입력하세요: "),
            "student_ID": create_student_id(), # 아이디 자동생성 하도록 변경
            "student_age": input("나이를 입력하세요: "),
            "student_name": input("이름을 입력하세요: "),
            "total_course_info": {
                "learning_course_info": get_learning_course_info_list(),
                "num_of_course_learned": input("과거수강 횟수를 입력하세요: "),
            }
        }
    )


def get_student_info():
    while True:
        menu = input("아래 메뉴를 선택하세요.\n1. 전체 학생정보 조회\n 검색 조건 선택\n2. ID 검색\n3. 이름 검색\n"
                     "4. 나이 검색\n5. 주소 검색\n6. 과거 수강 횟수 검색\n7. 현재 강의를 수강중인 학생\n"
                     "8.현재 수강 중인 강의명\n9. 현재 수강 강사\n10. 이전 메뉴\n메뉴를 선택하세요: ")

        if menu == '1':
            search_student_info_all()
        elif menu == '2':
            search_word = input("검색어를 입력하세요: ")
            search_student_info_id(search_word)
        elif menu == '3':
            search_word = input("검색어를 입력하세요: ")
            search_student_info_name(search_word)
        elif menu == '4':
            search_word = input("검색어를 입력하세요: ")
            search_student_info_age(search_word)
        elif menu == '5':
            search_word = input("검색어를 입력하세요: ")
            search_student_info_address(search_word)
        elif menu == '6':
            search_word = input("검색어를 입력하세요: ")
            search_student_info_learned(search_word)
        elif menu == '7':
            search_student_info_learning()
        elif menu == '8':
            search_word = input("검색어를 입력하세요: ")
            search_student_info_course(search_word)
        elif menu == '9':
            search_word = input("검색어를 입력하세요: ")
            search_student_info_teacher(search_word)
        break


def search_student_info_all():
    for dict in g_json_bigdata:
        print_student_info(dict)


def search_student_info_id(search_word):
    for dict in g_json_bigdata:
        if search_word in dict['student_ID']:
            print_student_info(dict)


def search_student_info_name(search_word):
    for dict in g_json_bigdata:
        if search_word in dict['student_name']:
            overlap_name.append(dict)
    if len(overlap_name) == 1:
        print_student_info(overlap_name)
    else:
        print("복수 개의 결과가 검색되었습니다.\n ----- 요약 결과 -----")
        for dict in overlap_name:
            print(">>학생 ID: %s, 학생 이름: %s" % (dict['student_ID'], dict['student_name']))


def search_student_info_age(search_word):
    for dict in g_json_bigdata:
        if search_word in dict['student_age']:
            print_student_info(dict)


def search_student_info_address(search_word):
    for dict in g_json_bigdata:
        if search_word in dict['student_address']:
            print_student_info(dict)


def search_student_info_learned(search_word):
    for dict in g_json_bigdata:
        if search_word == dict['total_course_info']['num_of_course_learned']:
            print_student_info(dict)


def search_student_info_learning():
    for dict in g_json_bigdata:
        if dict['total_course_info']['learning_course_info'] != '':
            print_student_info(dict)


def search_student_info_course(search_word):
    for dict in g_json_bigdata:
        if search_word == dict['total_course_info']['course_name']:
            print_student_info(dict)


def search_student_info_teacher(search_word):
    for dict in g_json_bigdata:
        if search_word == dict['total_course_info']['teacher']:
            print_student_info(dict)


def print_student_info(dict):
    print("*학생 ID: %s\n*이름: %s\n나이: %s\n*주소: %s\n수강 정보\n + 과거 수강 횟수: %s" % (dict['student_ID'], dict['student_name'], dict['student_age'], dict['address'], dict['total_course_info']['num_of_course_learned']))
    if dict['total_course_info']['learning_course_info'] != {}:
        print_course_info(dict)


def print_course_info(dict):
    print(" + 현재 수강 과목")
    for dict in dict['total_course_info']['learning_course_info']:
        print("  강의코드: %s\n  강의명: %s\n  강사: %s\n  개강일: %s\n  종료일: %s" % (dict['course_code'], dict['course_name'], dict['teacher'], dict['open_date'], dict['close_date']))


while True:
    with open('ITT_Student.json', encoding='UTF-8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)

    if json_big_data == []:
        with open('ITT_Student.json', 'w', encoding='utf-8') as outfile:
            readable_result = json.dumps(g_json_bigdata, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('ITT_Student.json SAVED')

    for dict in json_big_data:
        g_json_bigdata.append(dict)

    menu = input("\t\t<< JSON기반 학생 정보 관리 프로그램 >>\n1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n"
                 "4. 학생 정보삭제\n5. 프로그램 종료\n메뉴를 선택하세요: ")
    if menu == '5':
        break
    elif menu == '1':
        count += 1
        create_student_info()
    elif menu == '2':
        get_student_info()