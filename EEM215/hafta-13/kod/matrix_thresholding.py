from numpy.random import randint
from numpy.random import rand
import numpy as np

def matrix_threshold(M, threshold):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i,j] < threshold:
                M[i,j] = 0
            else:
                M[i,j] = 255
    return M

min_value, max_value = 0, 255
r, c = 5, 8
A = randint(min_value, max_value+1, (r,c))
B = np.round(255*rand(r,c))

print(f"A = {A}")
A_binary = matrix_threshold(A, 100)
print(f"A_binary = {A_binary}")
print(f"B = {B}")
B_binary = matrix_threshold(B, 50)
print(f"B_binary = {B_binary}")
print(f"A.dtype = {A.dtype}")
print(f"B.dtype = {B.dtype}")