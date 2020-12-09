# Implementation of function csv2mlregr() in Python
# Multiple linear regression model from csv data

from __future__ import print_function
import pandas as pd
from datamidware.pyalgo import multiple_linear_regr


def csv2mlregr(csv_file, x, y):
    """
    Model multiple linear regression from csv file.
    """

    try:
        # Read csv file in pandas DataFrame
        df = pd.read_csv(csv_file)
        print(df.head(5))

        multiple_linear_regr.multiple_linear_regr(df, x, y)

    except Exception as e:
        print('Error: {}'.format(str(e)))


if __name__ == "__main__":

    # Reading the data in
    csv_file = "../tests/test_data/FuelConsumption.csv"

    csv2mlregr(csv_file, ['ENGINESIZE','CYLINDERS', 'FUELCONSUMPTION_COMB'], "CO2EMISSIONS")
