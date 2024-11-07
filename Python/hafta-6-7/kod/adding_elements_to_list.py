names = ["Safa", "Mahmoud", "Abdullah", "Nour"] # ilk oluşturulan liste
print(f"names = {names}")
names.insert(1, "Tabarak") # 2. sıraya Tabarak'ı ekleyelim
print(f"names = {names}")
names.insert(0, "Çınay") # ilk sıraya Çınay'ı ekleyelim
print(f"names = {names}")
# Mahmoud'un yerine listeye Abdurrahman'ı listeye almaya karar verdik
names[3] = "Abdurrahman"
print(f"names = {names}")
# listenin sonuna Önder'i ekleyelim
names.append("Önder")
print(f"names = {names}")
# for döngüsü kullanarak listenin elemanlarını sırayla ekrana yazdıralım
for name in names:
    print(f"{name.upper()}")
# kendimiz index oluşturarak listenin elemanlarını sırayla ekrana yazdıralım
for i in range(len(names)):
    print(f"{i + 1}. {names[i].upper()}")