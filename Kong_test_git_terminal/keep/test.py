import numpy as np
arr = np.array([[2,4,9],[0,9,5]])
print(arr.ndim)
arr = arr.flatten()
print(arr)
arr.sort()
print(*arr)
