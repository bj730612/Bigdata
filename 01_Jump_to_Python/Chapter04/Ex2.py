def input_ingredient():
    ingredient = ""
    ingredient_list = []

    while ingredient != '종료':
        ingredient = input("안녕하세요. 원하시는 재료를 입력하세요.: ")
        if ingredient == '종료':
            break
        ingredient_list.append(ingredient)
    return ingredient_list


def make_sandwiches(ingredient_list):
    print("샌드위치를 만들겠습니다.")
    for i in ingredient_list:
        print("%s 추가합니다." %i)
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")


print("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.\n1. 주문\n2. 종료")
num = int(input("입력: "))
if num == 1:
    ingredient_list = input_ingredient()
    if ingredient_list != []:
        make_sandwiches(ingredient_list)