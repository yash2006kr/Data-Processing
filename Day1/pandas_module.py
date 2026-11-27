import pandas as pd
import numpy as np
from pandas.core import series
print(pd.__version__)
numbers = [10,0,-5,2,-8]
series1 = pd.Series(numbers)
print(series1)
print(type(series1))

indices = ['a','b','c','d','e']
series2 = pd.Series([1,2,3,4,5], index=indices)
print(series2)

currencies = {'$': "USD", '€': "Euro", '₹': "Rupee", '¥': "Yen", '₩': "Won"}
series3 = pd.Series(currencies)
print(series3)

array = np.arange(10,16)
series4 = pd.Series(array)
print(series4)

series5 = pd.Series(12)
print(series5)

