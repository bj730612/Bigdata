path = '.'
file_name = \\poll.txt

def read_content():
    f = open(path+file_name, 'r', encoding='utf-8')
    responses = f.readlines()

    print("< 현재 누적 응답 현황 >")
    for response in responses:
        print(response, end='')
    print('')
    f.close()

if os.path.isfile("poll.txt") == False:
    menu = int(input("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.\n"
           + "1. 종료 2. 새로운 파일 생성 3. 변경된 파일 경로 입력 : "))
    if menu == 1:
        print("프로그램 종료")
        break
    elif menu == 2:
        f = open('poll.txt', 'a', encoding='utf-8')
        while (True):
            msg = input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료): ")
            if msg == "종료":
                print("프로그램 종료")
                break
            else:
                name = input("이름을 입력해주세요: ")
                print("설문에 응답해 주셔서 감사합니다.")
                data = ("[%s] %s\n" % (name, msg))
                file.write(data)
    elif menu == 3:
        path = input("변경된 파일 경로를 입력하세요: ")
        print(read_content())

f.close()