import numpy as np
numbers = np.array([2, 7, -8, 12, 5, -34, 56, 15, -3])
print(f"numbers = {numbers}")
print(f"type(numbers) = {type(numbers)}")
print(f"numbers isimli numpy dizisinin uzunluğu {len(numbers)}.")
# numbers isimli numpy dizisinin elemanlarını dolaşarak negatif eleman sayısını bulalım
count, i = 0, 0
while i < len(numbers):
    if numbers[i] < 0:
        count += 1
    i += 1
print(f"numbers isimli numpy dizisinin içinde {count} tane negatif sayı var.")
