import pandas as pd
from sklearn import svm, metrics
and_input = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]
# 1. 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기
and_df = pd.DataFrame(and_input)
and_data = and_df.ix[:, 0:1]  # 데이터
and_label = and_df.ix[:, 2]   # 레이블
# 2. 데이터 학습과 예측하기
clf = svm.SVC()
clf.fit(and_data, and_label)
pre = clf.predict(and_data)
# 3. 정답률 구하기
ac_score = metrics.accuracy_score(and_label, pre)
print("정답률 =", ac_score)
