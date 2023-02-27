import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics


df = pd.read_csv('input.csv') 
print(df.shape)
df.describe()
target_column = ['n'] 
predictors = list(set(list(df.columns))-set(target_column))

print(df[predictors])
df.describe()
X = df[predictors].values
y = df[target_column].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=500)
print(X_train.shape); print(X_test.shape)

model_rf = RandomForestRegressor(n_estimators=500, oob_score=True, warm_start=True,random_state=50)
model_rf.fit(X_train, y_train) 
pred_train_rf= model_rf.predict(X_train)
df.to_csv('new_clean_file.csv')
print(r2_score(y_train, pred_train_rf))

pred_test_rf = model_rf.predict(X_test)
print(np.sqrt(mean_squared_error(y_test,pred_test_rf)))
print(r2_score(y_test, pred_test_rf))
print(X_test)
print(pred_test_rf)


def plotGraph(y_train,pred_train_rf,regressorName):
    if max(y_train) >= max(pred_train_rf):
        my_range = int(max(y_train))
    else:
        my_range = int(max(pred_train_rf))
    plt.scatter(range(len(y_train)), y_train, color='blue')
    plt.scatter(range(len(pred_train_rf)), pred_train_rf, color='red')
    plt.title(regressorName)
    plt.show()
    return


y_test = range(10)
y_pred = np.random.randint(0, 10, 10)

plotGraph(y_train, pred_train_rf, "test")


y_true = y_train
y_pred = pred_train_rf 

print('Mean Absolute Error (MAE):', metrics.mean_absolute_error(y_true, y_pred))
print('Mean Squared Error (MSE):', metrics.mean_squared_error(y_true, y_pred))
print('Root Mean Squared Error (RMSE):', metrics.mean_squared_error(y_true, y_pred, squared=False))
print('Mean Absolute Percentage Error (MAPE):', metrics.mean_absolute_percentage_error(y_true, y_pred))
print('Explained Variance Score:', metrics.explained_variance_score(y_true, y_pred))
print('Max Error:', metrics.max_error(y_true, y_pred))
print('Mean Squared Log Error:', metrics.mean_squared_log_error(y_true, y_pred))
print('Median Absolute Error:', metrics.median_absolute_error(y_true, y_pred))
print('R^2:', metrics.r2_score(y_true, y_pred))
print('Mean Poisson Deviance:', metrics.mean_poisson_deviance(y_true, y_pred))
print('Mean Gamma Deviance:', metrics.mean_gamma_deviance(y_true, y_pred))

y_r = df[target_column].values.ravel()
score_rf=cross_val_score(RandomForestRegressor(n_estimators = 50),X,y_r, cv = 10)

print(score_rf)
print('CV accuracy: %.3f +/- %.3f' % (np.mean(score_rf), np.std(score_rf)))
print("Avg :",np.average(score_rf))

print('Score: ', model_rf.oob_score_)