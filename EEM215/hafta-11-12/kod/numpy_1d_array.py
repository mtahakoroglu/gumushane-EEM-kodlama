import numpy as np
numbers = np.array([7, 12, -3, 4, -5])
print(f"numbers = {numbers}")
# listenin sonuna 16 sayısını ekleyelim
numbers = np.append(numbers, 16)
print(f"numbers = {numbers}")
# listenin sonuna 2 ekleyelim
numbers = np.append(numbers, 2)
print(f"numbers = {numbers}")
# listenin başına 9 ekleyelim
numbers = np.insert(numbers, 0, 9)
print(f"numbers = {numbers}")
# listenin başından ikinci sıraya 5 ekleyelim
numbers = np.insert(numbers, 1, 5)
print(f"numbers = {numbers}")
# listenin başından üçüncü elemanı silelim
numbers = np.delete(numbers, 2)
print(f"numbers = {numbers}")