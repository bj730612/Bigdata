class Restaurant:
    number_served = 0

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s이고 %s 전문점입니다." % (self.name, self.type))

    def open_restaurant(self):
        print("저희 %s 레스토랑이 오픈했습니다." % self.name)

    def reset_number_served(self, number):
        self.number_served = int(number)
        print("손님 카운팅을 0으로 초기화 하였습니다.")

    def increment_number_served(self,number):
        self.number_served += int(number)
        print("손님 %s명 들어오셨습니다. 자리를 안내해 드리겠습니다." % number)

    def check_customer_number(self):
        print("지금까지 총 %s명 손님께서 오셨습니다." % self.number_served)


number = 0
name_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")
name_type = name_type.split(" ")
name = name_type[0]
type = name_type[1]
res = Restaurant(name, type)
res.describe_restaurant()

open = input("레스토랑을 오픈하시겠습니까? (y/n)")
if open == 'y':
    res.open_restaurant()
    while number != '-1':
        number = input("어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) :")
        if number == '-1':
            break
        elif number == '0':
            res.reset_number_served(0)
        elif number == 'p':
            res.check_customer_number()
        elif int(number) < 0:
            print('다시 입력하세요.')
            continue
        else:
            res.increment_number_served(number)
