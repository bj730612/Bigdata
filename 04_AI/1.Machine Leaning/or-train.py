import pandas as pd
from sklearn import svm, metrics
# OR 연산
or_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
# 1. 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기
or_df = pd.DataFrame(or_input)
or_data = or_df.ix[:, 0:1]  # 데이터
or_label = or_df.ix[:, 2]   # 레이블
# 2. 데이터 학습과 예측하기
clf = svm.SVC()
clf.fit(or_data, or_label)
pre = clf.predict(or_data)
# 3. 정답률 구하기
ac_score = metrics.accuracy_score(or_label, pre)
print("정답률 =", ac_score)
