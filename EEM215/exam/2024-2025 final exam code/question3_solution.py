from numpy.random import randint
from numpy.random import rand
import numpy as np
minEleman, maxEleman, satir, sutun = -50, 50, 6, 10
A = randint(minEleman, maxEleman+1, (satir, sutun))
A = np.array([[9, 10, -50, 47, -24, -40, 33, -42, -1, -31], 
             [3, 20, -17, 16, -43, -30, 11, -27, -35, -7],
             [-4, 8, 48, 21, 38, -7, 17, -32, -7, 42],
             [-45, 20, 43, 23, 38, 44, -34, 35, -45, 31],
             [2, 46, 50, -8, 23, -5, 3, 23, 34, -11],
             [16, 10, -36, -33, 33, 32, -25, 6, 33, 5]])
a = A[-3, -4]; b = A[0, 0:3]; c = A[1:, -1]; d = A[:, 3]
e = A[0, -5:-1]; f = A[-1, 0:3]; G = A[1:-1, 0:3]; H = A[-2:, 4:6]
print(f"A = {A}"); print(f"a = {a}"); print(f"b = {b}")
print(f"c = {c}"); print(f"d = {d}"); print(f"e = {e}")
print(f"f = {f}"); print(f"G = {G}"); print(f"H = {H}")
# yukarıda rasgele oluşturulan A matrisini aynı değerlerle oluşturmak için
# aşağıdaki fonksiyonlardan hangisini kullanmalıyız? Birini seçiniz.
# a) A = ...*rand(..., ...)
# b) A = np.array([..., ....., ...], ..., [..., ....., ...])