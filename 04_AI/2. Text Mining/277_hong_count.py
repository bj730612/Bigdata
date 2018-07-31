import codecs
from konlpy.tag import Twitter
# 1. utf-8 인코딩으로 파일을 열고 글자를 출력하기
fp = codecs.open("hong.txt", "r", encoding="utf-8")
text = fp.read()
# 2. 텍스트 한 줄씩 처리하기
twitter = Twitter()
word_dic = {}
lines = text.split("\r\n")
for line in lines:
    malist = twitter.pos(line)
    for word in malist:
        if word[1] == "Noun": # 3. 명사 확인하기
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 # 카운트하기
# 4. 많이 사용된 명사 출력하기
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()