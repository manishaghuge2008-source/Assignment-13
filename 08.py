import numpy as np


a = np.random.randint(1, 101, (4, 4))

print("Matrix:")
print(a)

print("\n Shape:", a.shape)
print("Dimension:", a.ndim)
print("Total Elements:", a.size)
print("Data Type:", a.dtype)
print("Minimum Value:", a.min())
print("Maximum Value:", a.max())


