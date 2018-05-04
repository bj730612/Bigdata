#coding: cp949

names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(",")

#1
a=[ i[0] for i in names ]
print("김씨 : %d\n이씨 : %d\n"%(a.count("김"), a.count("이")))

#2
print(names.count("이재영"))

#3
uniq_names = list(set(names))
print(uniq_names)

#4
uniq_names.sort()
print(uniq_names)

