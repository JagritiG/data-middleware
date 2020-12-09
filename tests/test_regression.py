# Test Regression models : Simple Linear regression, multiple linear regression, polynomil regresssion, non-linear regression
import pytest
import numpy as np
from datamidware.pyalgo import linear_regression_ols


def test_linear_regression():

    # Observations
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    b = linear_regression_ols.linear_regression(x, y, "Simple Linear Regression", "Independent Variable",
                                            "Dependent Variable", "./tests/test_result/Simple_Linear_Regression.png")
    assert [b[0], b[1]] == [1.2363636363636363, 1.1696969696969697]


