import numpy as np

# a) 1D array of 10 random numbers between 0 and 1
a = np.random.rand(10)
print("a) Random numbers between 0 and 1:")
print(a)

# b) 3x3 matrix of random numbers from standard normal distribution
b = np.random.randn(3, 3)
print("\nb) 3x3 Random matrix (Standard Normal Distribution):")
print(b)

# c) 4x5 array of random integers between 10 and 50
c = np.random.randint(10, 51, (4, 5))
print("\nc) 4x5 Random Integer Matrix (10 to 50):")
print(c)