#coding: cp949

names = "������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������".split(",")

#1
a=[ i[0] for i in names ]
print("�达 : %d\n�̾� : %d\n"%(a.count("��"), a.count("��")))

#2
print(names.count("���翵"))

#3
uniq_names = list(set(names))
print(uniq_names)

#4
uniq_names.sort()
print(uniq_names)

