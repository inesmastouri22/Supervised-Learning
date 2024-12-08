# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/166PqSYMjgRBmn9hi3EAcGC2cnQpDSeHV
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

salary_data = pd.read_csv('Salary_Data.csv')

x = salary_data.iloc[:,:-1].values
y = salary_data.iloc[:,1].values

sns.barplot(x='YearsExperience', y='Salary', data=salary_data)

sns.regplot(x='YearsExperience', y='Salary', data=salary_data)

sns.displot(salary_data['YearsExperience'], kde=False, bins=10)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
y_pred

plt.scatter(x_train, y_train, color='blue')
plt.plot(x_train, regressor.predict(x_train), color='red')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(x_test, y_test, color='blue')
plt.plot(x_train, regressor.predict(x_train), color='red')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
print('MSE:', metrics.mean_squared_error(y_test, y_pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))



