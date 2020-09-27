import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


sns.set(style="darkgrid")
titanic = pd.read_csv("/Users/santanusarma/Dropbox/Jagriti/Programming/Data Analysis/data_integration_middleware/dataware/tests/test_data/titanic_short.csv")
ax = sns.countplot(x="Pclass", data=titanic)

plt.show()
