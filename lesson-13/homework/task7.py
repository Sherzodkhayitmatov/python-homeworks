import numpy as np 

matrix = np.random.random((5,5))
normalize = matrix - np.min(matrix) / np.max(matrix) - np.min(matrix)
print(matrix)
print(normalize)