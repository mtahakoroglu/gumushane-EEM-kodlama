names = ["Tabarak", "Abdurrahman", "Sefa", "Abdullah", "Hussein", "Nour"]
ages = [22, 23, 21, 18, 18, 19]
weights = [42.1, 65.4, 70.5, 80.4, 68.7, 45.3]
birthplaces = ["Irak", "Çad", "Gümüşhane", "Bursa", "Yemen", "Lübnan"]
attendance = [True, False, True, True, False, True]
# şimdi listeleri ekrana yazdıralım
print(f"İsimler: {names}")
print(f"Yaşlar: {ages}")
print(f"Ağırlıklar: {weights}")
print(f"Doğum Yerleri: {birthplaces}")
print(f"Yoklama: {attendance}")
# şimdi listelerden elemanları tek tek seçerek ekrana yazdıralım
for i in range(len(names)):
    if attendance[i]:
        print(f"Doğum yeri {birthplaces[i]} olan {names[i]}, {ages[i]} yaşında olup {weights[i]} kg ağırlığındadır.")
    else:
        print(f"{names[i]} bugün derste yoktur.")