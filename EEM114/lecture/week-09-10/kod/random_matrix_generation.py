from numpy.random import randint

r, c = 3, 5 # satır ve sütun sayısı
minA, maxA = -10, 11 # matrisin elemanlarının alabileceği minimum ve maksimum değerler
A = randint(minA, maxA, (r, c)) # r x c boyutunda A matrisini oluştur
print(f"A:\n{A}") # A matrisini ekrana yazdır