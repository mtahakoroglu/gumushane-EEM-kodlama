<h3>FONKSİYONLAR - DEVAM</h3>

<p align="justify">Bir matrisin minimum ve maksimum elemanlarını ve negatif ve pozitif eleman sayılarını bulan <b>matrix_stats()</b> isimli bir fonksiyon yazalım. Koddaki boşlukları doldurunuz.</p>

<b>finding_matrix_statistics.py</b>

```
from __________ import __________

_____ matrix_stats(__________):
    # Buraya fonksiyonu yazınız...

# elemanları en az -10 en fazla 10 olabilen 4 satır 10 sütunluk rasgele matris üretelim
_____, ______, ______, ______ = ____, ____, ____, ____
A = __________(min, max, (row, col))
mi, ma, ne, nn, nz, np = matrix_stats(A)
search_for = 5
n_search_for = (A == search_for).sum()
print(f"Matris A\n{A}"); print(f"Minimum değer: {mi}")
print(f"Maksimum değer: {ma}"); print(f"Toplam eleman sayısı: {ne}")
print(f"Negatif eleman sayısı: {nn}")
print(f"Sıfır sayısı: {nz}")
print(f"Pozitif eleman sayısı: {np}")
print(f"Matrisdeki {search_for} elemanı sayısı: {n_search_for}")
```

