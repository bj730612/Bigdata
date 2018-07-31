from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
# 1. 키와 몸무게 데이터 읽어 들이기
tbl = pd.read_csv("bmi.csv")
# 2. Column(열)을 자르고 정규화하기
label = tbl["label"]
w = tbl["weight"] / 100 # 최대 100kg라고 가정
h = tbl["height"] / 200 # 최대 200cm라고 가정
wh = pd.concat([w, h], axis=1)
# 3. 학습 전용 데이터와 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test = train_test_split(wh, label)
# 4. 데이터 학습하기
clf = svm.SVC()
clf.fit(data_train, label_train)
# 5. 데이터 예측하기
predict = clf.predict(data_test)
# 6. 결과 테스트하기
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)
