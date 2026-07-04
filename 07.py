import numpy as np


A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])


print("Matrix Addition:")
print(A + B)


print("\n Matrix Multiplication:")
print(np.dot(A, B))


print("\n Element-wise Multiplication:")
print(A * B)