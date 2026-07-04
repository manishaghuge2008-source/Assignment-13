import numpy as np


a = np.random.randint(1, 51, 20)

b = a.reshape(4, 5)

print("4x5 Matrix:")
print(b)


print("\n Sum:", b.sum())


print("Mean:", b.mean())


print("Standard Deviation:", b.std())

print("Maximum value in each row:")
print(b.max(axis=1))

