import numpy as np  

matrix = np.random.random((5,5))
row = np.sum(matrix, axis=1)
column = np.sum(matrix, axis=0)
print(matrix)
print(row)
print(column)