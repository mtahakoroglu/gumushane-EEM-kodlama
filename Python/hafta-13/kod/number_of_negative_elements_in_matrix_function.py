import numpy as np
from numpy.random import randint

def num_of_neg_elements(A):
    return np.int32(A < 0).sum()

r, c = 5, 8
A = randint(-10, 11, (r, c))

print(A)
print(f"Matristeki negatif eleman sayısı: {num_of_neg_elements(A)}")