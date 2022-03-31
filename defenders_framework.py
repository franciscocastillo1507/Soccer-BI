
"""Defenders Framework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kT7rLmDcvdndfBx_wZrbzFjuxUKDo0hq
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Defenders.csv')

df_y = df['Goals Conceded'].values.reshape(-1,1)
df_x = df['Appearances'].values.reshape(-1,1)
df_xTwo = df['Fouls Committed'].values.reshape(-1,1)
print(df_x.shape, df_y.shape)

"""Train a model with it"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


poly = PolynomialFeatures(2, include_bias=False)
poly_att = poly.fit_transform(df_x)

X_train, X_test, y_train, y_test = train_test_split(poly_att, df_y, test_size=0.4, random_state=55)
# Create linear regression object
model = LinearRegression()

# Train the model using the training sets
model.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = model.predict(X_test)

# The coefficients
print('Coefficients: \n', model.coef_)
# The mean squared error
print('Mean squared error: %.2f'
#       % mean_squared_error(y_test, y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
#       % r2_score(y_test, y_pred))

# Plot the predicitons
x_test_val = [item[0] for item in X_test]
plt.figure(figsize=(10,6))
plt.scatter(x_test_val, y_test, color='#122423')
plt.scatter(x_test_val, y_pred, color='#F96167')
plt.xlabel("Appearances")
plt.ylabel('Goals Conceded')
plt.show()



# Commented out IPython magic to ensure Python compatibility.
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


poly = PolynomialFeatures(2, include_bias=False)
poly_att = poly.fit_transform(df_xTwo)

X_train, X_test, y_train, y_test = train_test_split(poly_att, df_y, test_size=0.4, random_state=55)
# Create linear regression object
model = LinearRegression()

# Train the model using the training sets
model.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = model.predict(X_test)

# The coefficients
print('Coefficients: \n', model.coef_)
# The mean squared error
print('Mean squared error: %.2f'
#       % mean_squared_error(y_test, y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
#       % r2_score(y_test, y_pred))

# Plot the predicitons
x_test_val = [item[0] for item in X_test]
plt.figure(figsize=(10,6))
plt.scatter(x_test_val, y_test, color='#122423')
plt.scatter(x_test_val, y_pred, color='#F96167')
plt.xlabel("Foul Commited")
plt.ylabel('Goals Conceded')
plt.show()