import pandas as pd

# Read the CSV file instead of an Excel file
data1 = pd.read_csv('x.csv', header=None)
data2 = pd.read_csv('y.csv', header=None)


print(data1.shape)
print(data2.shape)