import pandas as pd

dates = pd.date_range('2026-01-01', '2026-01-05')
print(dates)
numbers = [10, 20, 30, 40, 50]
series1 = pd.Series(numbers, index=dates)
print(series1)
print(series1.values)
print(series1.index)

series2 = pd.Series(numbers)
print(series2)
print(series2[2])
print(series2[[2,3]])

print(series2.count())
print(series2.sum())
print(series2.max())
print(series2.min())