import pandas as pd
import numpy as np


# print(pd.__version__)
# print(np.__version__)


# Literal List
series1 = pd.Series([1,2,3,4,5])

# print(series1)
# print("================")
# print(series1[1:3])

# Numpy arary
# arr = np.arange(10,20)
# series2 = pd.Series(arr)
# print(series2)
# print(series2[5:])

series2 = pd.Series([1,2,3,4,5], index=['A','B', 'C','D','E'])
print(type(series2))

print(series1.iloc[0])
print(series1.iloc[1:4])
print(series1.index)