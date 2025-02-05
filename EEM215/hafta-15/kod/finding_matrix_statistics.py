from numpy.random import randint

def matrix_stats(matrix):
    mi = matrix.min() # minimum değer
    ma = matrix.max() # maksimum değer
    ne = matrix.size # matrisin eleman sayısı
    nn = (matrix < 0).sum() # matrisin negatif eleman sayısı
    nz = (matrix == 0).sum() # matrisin sıfır eleman sayısı
    np = (matrix > 0).sum() # matrisin pozitif eleman sayısı
    return mi, ma, ne, nn, nz, np

min, max, row, col = -10, 10, 4, 10
A = randint(min, max, (row, col))
mi, ma, ne, nn, nz, np = matrix_stats(A)
search_for = 5
n_search_for = (A == search_for).sum()
print(f"Matris A\n{A}"); print(f"Minimum değer: {mi}")
print(f"Maksimum değer: {ma}"); print(f"Toplam eleman sayısı: {ne}")
print(f"Negatif eleman sayısı: {nn}")
print(f"Sıfır sayısı: {nz}")
print(f"Pozitif eleman sayısı: {np}")
print(f"Matrisdeki {search_for} elemanı sayısı: {n_search_for}")