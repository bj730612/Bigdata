def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)


def verify_customer(name, old, customer_levels='silver'):
    print("고객님 성함은 %s입니다." %name)
    print("고객님의 나이는 %d살입니다." %old)

    if customer_levels == 'silver':
        print("고객님의 등급은 %s입니다.\n" %customer_levels)
    if customer_levels == 'gold':
        print("고객님의 등급은 %s입니다.\n" %customer_levels)
    if customer_levels == 'platinum':
        print("고객님의 등급은 %s입니다.\n" %customer_levels)


verify_customer("안철수", 56, 'gold')
verify_customer("이효리", 34, 'platinum')
verify_customer("박응용", 27)