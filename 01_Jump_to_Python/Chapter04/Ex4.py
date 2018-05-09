f = open('방명록.txt', 'r', encoding='utf-8')
visitor_list = f.readlines()


def search_visitor(name):
    f = open('방명록.txt', 'a', encoding='utf-8')
    for line in visitor_list:
        line = line.replace('\n', '')
        temp_name, temp_birth = map(str, line.split(' '))
        if name == temp_name:
            print(line + '님 다시 방문해 주셔서 감사합니다. 즐거운 시간 되세요.')
            break
    if name != temp_name:
        birth = input('생년월일을 입력하세요. (예:801212):')
        print(name + "님 환영합니다. 아래 내용을 입력하셨습니다.")
        print(name + " " + birth)
        data = ("\n" + name + " " + birth)
        f.write(data)


name = input('이름을 입력하세요. :')
search_visitor(name)
