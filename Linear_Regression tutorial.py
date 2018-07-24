import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2] 
y = iris.target

# Create a linear regression object
regr = linear_model.LinearRegression()

# Fit the linear regression to our data
regr.fit(X, y)

# Print model coefficients and intercept
print "Intercept: \n", regr.intercept_
print "Coefficients: \n", regr.coef_

## Plot the data
# Prepare the plot
plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the data
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

## Read in text file
mystery_data = pd.read_csv('mystery_data.txt', sep=" ", header=0)

## Look at first 5 rows of data
#print mystery_data.head(5)

## Save variables
x = np.array(mystery_data[['x']])
u = np.array(mystery_data[['u']])
y = np.array(mystery_data[['y']])
z = np.array(mystery_data[['z']])

## Run linear regression
regr = linear_model.LinearRegression()

# Fit the linear regression to our data
X = np.column_stack((x, u, z))
regr.fit(X, y)

# Print model coefficients and intercept
print "Intercept: \n", regr.intercept_
print "Coefficients: \n", regr.coef_


