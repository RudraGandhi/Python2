""" Reading CSV file using pandas """

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('auto-mpg.csv')
""" print(data.set_index('car name')) """
print(data)
horsepower = data['horsepower']
weight = data['weight']
plt.plot(horsepower,weight)
plt.show()
""" print(data.T)
This will transpose your data """
""" print(data.dtypes)
print(data.size)
print(data.shape)
print(data['mpg'].shape)
print(data.ndim)
print(data.columns)
print(data.index)
print(type(data)) """