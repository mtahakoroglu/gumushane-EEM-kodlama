names = ['Willy', 'Arhan', 'Mustafa', 'Abdullah', 'Jesuno', 'Bonaventura', 
         'Manuel', 'Abdulrahim', 'Ziya', 'Rukiye', 'Taha', "İbrahim"]
print(f"Listenin ilk hâli = {names}")
print(f"İsimler listesinde {len(names)} eleman vardır.")
# isim listesinde harf sayısı 6 ve daha fazla olan isimleri 
# listeden atmak istiyorum ama attiğim isimleri yeni bir listede
# tutmak istiyorum ve bunu pop() metodu ile yapmak istiyorum
exported_names, k = [], 0
while k < len(names):
    if len(names[k]) >= 6:
        exported_names.append(names.pop(k))
    else:
        k += 1
print(f"Listenin son hâli = {names}")
print(f"İsimler listesinin son hâlinde {len(names)} eleman vardır.")
print(f"Çıkarılan isimler = {exported_names}")
print(f"Çıkarılanlar listesinde {len(exported_names)} eleman vardır.")