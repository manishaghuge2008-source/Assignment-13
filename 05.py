import numpy as np


a = np.random.rand(10)
print("a) Random numbers between 0 and 1:")
print(a)


b = np.random.randn(3, 3)
print("\n b) 3x3 Random matrix (Standard Normal Distribution):")
print(b)


c = np.random.randint(10, 51, (4, 5))
print("\n c) 4x5 Random Integer Matrix (10 to 50):")
print(c)

