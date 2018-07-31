import numpy as np
import pandas as pd
from statsmodels.formula.api import ols

housing = pd.read_csv('Housing.csv', sep=',', header=0)

housing['housing_driveway'] = np.where(housing['driveway'] == 'yes', 1., 0.)
housing['housing_recroom'] = np.where(housing['recroom'] == 'yes', 1., 0.)
housing['housing_fullbase'] = np.where(housing['fullbase'] == 'yes', 1., 0.)
housing['housing_gashw'] = np.where(housing['gashw'] == 'yes', 1., 0.)
housing['housing_airco'] = np.where(housing['airco'] == 'yes', 1., 0.)
housing['housing_prefarea'] = np.where(housing['prefarea'] == 'yes', 1., 0.)

my_formula = 'price ~ lotsize + bedrooms + bathrms + stories + housing_driveway + housing_recroom + housing_fullbase'\
             ' + housing_gashw + housing_airco + garagepl + housing_prefarea'
lm = ols(my_formula, data=housing).fit()

dependent_variable = housing['price']
independent_variables = housing[housing.columns.difference(['price', 'driveway', 'recroom', 'fullbase', 'gashw',
                                                            'airco', 'prefarea'])]

new_observations = housing.ix[housing.index.isin(range(10)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score, 2) for score in y_predicted]

print("\nCoefficients:\n%s" % lm.params)

count = 0
right_count = 0

for predict in y_predicted_rounded:
    count += 1
    if predict * 1.1 >= housing['price'][y_predicted_rounded.index(predict)] >= predict * 0.9:
        print('%d번째 샘플링 데이터 예측결과: %f, 실제가격: %f = > 정답'
              % (count, predict, housing['price'][y_predicted_rounded.index(predict)]))
        right_count += 1
    else:
        print('%d번째 샘플링 데이터 예측결과: %f, 실제가격: %f = > 오답'
              % (count, predict, housing['price'][y_predicted_rounded.index(predict)]))

print('<분석 결과 요약>')
print('관측계수: %d' % count)
print('예측값 정답 허용 범위: 실제값의 +- 10.0%')
print('정답률: %d / %d = %d%%' % (right_count, count, right_count/count*100))
