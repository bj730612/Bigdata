from sklearn import model_selection, svm, metrics
# 1. CSV 파일을 읽어 들이고 가공하기
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels": labels, "images": images}
data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")
# 2. 학습하기
clf = svm.SVC()
clf.fit(data["images"], data["labels"])
# 3. 예측하기
predict = clf.predict(test["images"])
# 4. 결과 확인하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)

# precision : 데이터셋에 존재하는 모든 라벨(종속변수)
# support : 전체 검증 데이터 개수
# recall : 재현율
# f1-score : 정밀도(precision)과 재현율(recall)의 가중조화 평균
