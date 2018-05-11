class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        restaurant_name = name
        cuisine_type = type
        print("저희 레스토랑 명칭은 %s이고 %s 전문점입니다." % (restaurant_name, cuisine_type))

    def open_restaurant(self):
        restaurant_name = name
        print("저희 %s 레스토랑이 오픈했습니다." % restaurant_name)

    def __del__(self):
        print("%s 레스토랑 문닫습니다." % self.name)


res = []

for i in range(0, 3):
    name_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")
    name_type = name_type.split(" ")
    name = name_type[0]
    type = name_type[1]

    res.append(Restaurant(name, type))
    res[i].describe_restaurant()
    res[i].open_restaurant()

print("저녁 10시가 되었습니다. \n")