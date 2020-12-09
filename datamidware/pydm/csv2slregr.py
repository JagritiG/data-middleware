# Implementation of function csv2slregr() in Python:
# Simple linear regression model from csv data
from __future__ import print_function
import pandas as pd
from datamidware.pyalgo import linear_regression


def csv2slregr(csv_file, x, y, x_label=None, y_label=None, filename=None, show=True):
    """
    Model simple linear regression from csv file.
    """

    try:
        # Read csv file in pandas DataFrame
        df = pd.read_csv(csv_file)
        print(df.head(5))

        linear_regression.linear_regression(df, x, y, x_label=x_label, y_label=y_label, filename=filename, show=show)

    except Exception as e:
        print('Error: {}'.format(str(e)))


if __name__ == "__main__":

    # Reading the data in
    csv_file = "../tests/test_data/FuelConsumption.csv"

    csv2slregr(csv_file, "ENGINESIZE", "CO2EMISSIONS", "Engine Size", "Co2 Emission", "csv_EngineSize_vs_Co2Emission_.png")
