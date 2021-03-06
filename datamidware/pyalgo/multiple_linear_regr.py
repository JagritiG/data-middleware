# Implementation of Multiple linear regression using scikit-learn
# OLS can find the best parameters using of the following methods:
# Solving the model parameters analytically using closed-form equations
# Using an optimization algorithm (Gradient Descent, Stochastic Gradient Descent, Newton’s Method)

# Importing required packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def multiple_linear_regr(df, x, y):
    """
    Multiple linear regression uisng least squares.
    Prints coefficient, y-intercept, and evaluation metrics:
    Mean absolute error,  Mean squared error, Residual sum of squares (MSE), variance score
    :param df: pandas data frame
    :param x: List of independent variables (features)
    :param y: dependent variable
    :return:
    """

    # Creating train and test dataset: Train/Test Split
    # Lets split our dataset into train and test sets, 80% of the entire data for training, and the 20% for
    # testing. We create a mask to select random rows using np.random.rand() function:
    msk = np.random.rand(len(df)) < 0.8
    train = df[msk]
    test = df[~msk]

    # Modeling with training set
    train_x = np.asanyarray(train[[i for i in x]])
    train_y = np.asanyarray(train[[y]])

    # Model initialization
    regression_model = LinearRegression()
    regression_model.fit(train_x, train_y)

    # Get the coefficient and y-intercept
    print("Coefficient and y-intercept:")
    print("Coefficient: {}".format(regression_model.coef_))
    print("Intercept: {}".format(regression_model.intercept_))

    # Predict the response, based on test set
    test_x = np.asanyarray(test[[i for i in x]])
    test_y = np.asanyarray(test[[y]])
    y_pred = regression_model.predict(test_x)

    # Evaluate the model
    # There are different model evaluation metrics to calculate the accuracy of the model
    # Calculate evaluation metrics
    mae = mean_squared_error(test_y, y_pred)
    rmse = np.mean(np.absolute(y_pred - test_y))
    mse = np.mean((y_pred - test_y) ** 2)
    var = regression_model.score(test_x, test_y)

    print("\nEvaluation metrics:")
    print("Mean absolute error: {:.2f}".format(mae))
    print("Mean squared error: {:.2f}".format(rmse))
    print("Residual sum of squares (MSE): {:.2f}".format(mse))
    print("Variance score: {:.2f}".format(var))


if __name__ == "__main__":

    # Reading the data in
    df = pd.read_csv("../tests/test_data/FuelConsumption.csv")
    # print(df.head())
    # print(df.columns)

    # Select some features to explore more
    # Features taken: 'ENGINESIZE', 'CO2EMISSIONS'
    cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
    # print(cdf.head(10))

    # plot features using scatterplot
    plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show(block=False)
    plt.pause(3)
    plt.close()

    # multiple_linear_regr(cdf, ['ENGINESIZE', 'CYLINDERS'], "CO2EMISSIONS")

    multiple_linear_regr(cdf, ['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB'], "CO2EMISSIONS")

