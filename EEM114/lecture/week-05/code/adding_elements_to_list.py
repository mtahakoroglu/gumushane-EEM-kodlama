names = ["Arhan", "Mustafa", "Abdullah", "Jesuno", 
         "Bonaventura", "Abdulrahim", "Ziya"]
print(f"names = {names}")
print(f"İsimler listesinde {len(names)} eleman vardır.")
# listenin sonuna Rukiye'yi ekleyelim
names.append("Rukiye")
print(f"names = {names}")
# listenin başına Willy'i ekleyelim
names.insert(0, "Willy")
print(f"names = {names}")
# listenin sondan 3. sırasına Manuel'i ekleyelim
names.insert(-3, "Manuel")
print(f"names = {names}")
# listenin sonuna Taha'yı append() kullanmadan ekleyelim
names.insert(len(names), "Taha")
print(f"names = {names}")
# Abdullah'ı listeden çıkarıp Umut'u koyalım
names[3] = "Umut"
print(f"names = {names}")