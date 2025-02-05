names = ["Önder", "Safa", "Abdullah"]
print(f"names = {names}")
# listenin sonuna yeni bir isim ekleyelim
names.append("Çınay")
print(f"names = {names}")
# listenin sonuna bir isim daha ekleyelim
names.append("Cindy")
print(f"names = {names}")
# listenin başına yeni bir isim ekleyelim
names.insert(0, "Abdurrahman")
print(f"names = {names}")
# listenin başından ikinci sıraya yeni bir isim ekleyelim
names.insert(1, "Sefa")
print(f"names = {names}")
# listenin başından üçüncü sıradaki ismi silelim
names.pop(2)
print(f"names = {names}")