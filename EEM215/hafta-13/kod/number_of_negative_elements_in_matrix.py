from numpy.random import randint
r, c = 5, 8
A = randint(-10, 11, (r, c))

count = 0
for i in range(r): # satırı dolaş
    for j in range(c): # sütunu dolaş
        if A[i, j] < 0:
            count += 1

print(A)
print(f"Matristeki negatif eleman sayısı: {count}")