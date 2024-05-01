""" Data Frame """

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = [['rudra',19,25000],['malav',20,10000],['mihir',20,5000]]
""" data = {'Name':['rudra','malav','mihir'],'Age':[19,20,20],'Salary':[25000,10000,5000]} """
""" you can make dataframe in two ways by making 2-d list or list of column name in dictionary"""

index = []
for i in range(0,len(data),1):
    index.append(data[i][0])

dataFrame = pd.DataFrame(data,columns=['Name','Age','Salary'],index=index)

print(dataFrame)