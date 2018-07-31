# 목적 : 이탈 고객사이에서 고정변수의 평균이 똑같을 확률 구하기
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

def inverse_logit(model_formula):
    from math import exp
    return (1.0 / (1.0 + exp(-model_formula))) * 100.0

churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
dependent_variable = churn['churn01']
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + churn['intl_charge']


independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

at_means = float(logit_model.params[0]) + float(logit_model.params[1])\
           + float(logit_model.params[2]) + float(logit_model.params[3])

print(churn['account_length'].mean())
print(churn['custserv_calls'].mean())
print(churn['total_charges'].mean())
print(at_means)
print("Probability of churn when independent variables are at their mean Values: %.2f" % inverse_logit(at_means))
