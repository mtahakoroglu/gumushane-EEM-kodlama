from numpy.random import randint

def matrix_stats(A):
    mi = A.min()
    ma = A.max()
    ne = A.size
    nn = (A < 0).sum()
    nz = (A == 0).sum()
    np = (A > 0).sum()
    return mi, ma, ne, nn, nz, np

# elemanları en az -10 en fazla 10 olabilen 4 satır 10 sütunluk rasgele matris üretelim
mi, ma, row, col = -10, 10, 4, 10
A = randint(mi, ma, (row, col))
mi, ma, ne, nn, nz, np = matrix_stats(A)
search_for = 5
n_search_for = (A == search_for).sum()
print(f"Matris A\n{A}"); print(f"Minimum değer: {mi}")
print(f"Maksimum değer: {ma}"); print(f"Toplam eleman sayısı: {ne}")
print(f"Negatif eleman sayısı: {nn}")
print(f"Sıfır sayısı: {nz}")
print(f"Pozitif eleman sayısı: {np}")
print(f"Matrisdeki {search_for} elemanı sayısı: {n_search_for}")