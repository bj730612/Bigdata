f = open('연습생.txt', 'r', encoding='utf-8')
candidate_list = f.readlines()


def show_candidates(candidate_list):
    for line in candidate_list:
        print(line, end="")
    print("")


def make_idol(candidate_list):
    for line in candidate_list:
        line = line.replace("\n", " ")
        if not line:
            break
        print("신예 아이돌 " + line + "인기 급상승")
    print("")


def make_world_star(candidate_list):
    for line in candidate_list:
        line = line.replace("\n", " ")
        if not line:
            break
        print("아이돌 " + line + "월드스타 등극")
    print("")


show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)
