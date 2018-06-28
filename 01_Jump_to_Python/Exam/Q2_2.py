f = open('poll.txt', 'a', encoding='utf-8')
while True:
    msg = input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료): ")
    if msg == "종료":
        print("프로그램 종료")
        break
    else:
        name = input("이름을 입력해 주세요: ")
        print("설문에 응답해 주셔서 감사합니다.")
        data = ("[%s] %s\n" % (name, msg))
        f.write(data)
f.close()