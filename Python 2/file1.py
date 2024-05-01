""" Data Series """

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

arr = np.array([1,2,3,4])
dataSeries = pd.Series(arr,copy=True)
""" Series is class of Pandas which takes list or dictionary as data and make it in series form (column) """

dataSeries.iloc[0] = 99
""" iloc[index] is used tochange the value at particular index if copy parameter is set False then it will change value in dataseries as well as in the data that pass in and if the copy is set True then it will oly change in dataseries"""
print(arr)
print(dataSeries)