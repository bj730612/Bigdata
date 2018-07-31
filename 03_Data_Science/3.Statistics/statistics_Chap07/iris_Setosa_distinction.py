import numpy as np
import pandas as pd
import statsmodels.api as sm

print('빅데이터 로드중..')
iris = pd.read_csv('iris.csv', sep=',', header=0)

print('분석용 빅데이터 가공중..')
iris.columns = iris.columns.str.replace('.', '_')
iris['is_Setosa'] = np.where(iris['variety'] == 'Setosa', 1., 0.)

print('빅데이터 통계 분석 모델 생성중..')
dependent_variable = iris['is_Setosa']
independent_variables = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()

print('테스트 데이터 선별 중..')

print('샘플링 데이터 예측 테스트 중')
print('6개 샘플링 데이터 리스트')
new_observations = iris.ix[iris.index.isin([48, 49, 50, 51, 52, 53]), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
print(new_observations_with_constant)

print('예측 결과 분석 중')
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]

no = 0
count = 0
right_count = 0
sample_list = [48, 49, 50, 51, 52, 53]

print(y_predicted_rounded)

for predict in y_predicted_rounded:
    if predict > 0.5:
        if predict == iris['is_Setosa'][sample_list[y_predicted_rounded.index(predict)]]:
            print('%d번째 샘플링 데이터 예측 결과 1.000000 : Setosa 확실 => 정답' % count)
            right_count += 1
        else:
            print('%d번째 샘플링 데이터 예측 결과 1.000000 : Setosa 확실 => 오답' % count)
    else:
        if predict == iris['is_Setosa'][sample_list[y_predicted_rounded.index(predict)]]:
            print('%d번째 샘플링 데이터 예측 결과 0.000000 : Setosa 아닌 다른 품종 => 정답' % count)
            right_count += 1
        else:
            print('%d번째 샘플링 데이터 예측 결과 0.000000 : Setosa 아닌 다른 품종 => 오답' % count)
    count += 1

print('<분석 결과 요약>')
print('관측계수: %d' % count)
print('정답률: %d / %d = %d%%' % (right_count, count, right_count / count * 100))
