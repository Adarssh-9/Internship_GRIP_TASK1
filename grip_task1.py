# -*- coding: utf-8 -*-
"""GRIP_TASK1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1md8PwGTIeaZPoNOX_BDt3IbT3ISenaOx

## **Prediction using Supervised ML**
This is a part of GRIPS MAY2021 Internship Program

Data set available on http://bit.ly/w-data
### Basic Linear Regression to predict score if a student studies for 9.25 hrs/ day

---
# By *Adarssh P N*
"""

# Commented out IPython magic to ensure Python compatibility.
#importing the required libraries

import pandas as pd #used for CSV
import numpy as np
import matplotlib.pyplot as plt  
# %matplotlib inline

# Reading the data set from the url given
url_link="http://bit.ly/w-data"
try:
  org_data=pd.read_csv(url_link)
except:
  print("Error occurred")
print('Data fetch sucessful')

#displaying the data
org_data.head()

"""### To Plot the given data set as a scatted plot so that we get a brief understanding about the relation between hours and Scores

"""

org_data.plot(x='Hours',y='Scores', style = 'ro')
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()

"""**From the above graph we can see that the realationship between the hours studied and the marks are directly proportional.**

## **Preparing the data**

Converting the data into attributes and labels
"""

X = org_data.iloc[:,:-1].values #choosing all colums and last but one row
Y = org_data.iloc[:,1].values #extracting the Y axis values
print(X,Y)

"""Spliting the data into two- training and test data set using the *Scikit-Learn built-in method*"""

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)

"""## **Training**

Here we shall be using the Linear Regression algo to train
"""

from sklearn.linear_model import LinearRegression
reggr=LinearRegression()
reggr.fit(X_train, Y_train)
print('Traning successful')

reg_line = reggr.coef_*X+reggr.intercept_ #reading the regression line

#plotting data by overlapping on the scattered data plot
plt.scatter(X,Y)
plt.plot(X,reg_line)
plt.show()

"""## **Predictions**
After training the model, we now make the predictions


"""

#here we set 30% of the actual data for testing purpose
#print(X_test)
Y_pred= reggr.predict(X_test)#predicting the scores by passing the hours studied

"""Comparing the actual and predicted data"""

prd_data = pd.DataFrame({'Acutal data' : Y_test, 'Predicted data': Y_pred})
print(prd_data)

"""**Testing the model with the data given**"""

#study hours per day
hours = [[9.25]]
q_pred = reggr.predict(hours)
print('Study hours: {}'.format(hours[0][0]))
print('Predicted Score: {}'.format(q_pred[0]))

"""## **Model Evaluation**
To find the performance of the model is crucial. There are various metrics to evaulate the model, here we have used the following

1.   Mean Absolute Error(MAE)
2.   Root Mean Square Error(RMSE)


"""

from sklearn import metrics  
import math # to calculate RMS
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, Y_pred)) 
print('Root Mean Square Error:', math.sqrt(metrics.mean_squared_error(Y_test, Y_pred)))