names = ["Abdullah", "sefa", "selin", "cindy", "patrick", "SAFA", "destinee"] # Bir Python listesi
print(f"names = {names}")
print(f"names isimli listenin uzunluğu {len(names)}.")
# names isimli listenin elemanlarını dolaşarak 'S' ile başlayan isim sayısını bulalım
count = 0
for i in range(len(names)):
    if names[i][0].upper() == 'S':
        count += 1
print(f"Verilen listede {count} adet isim 'S' ile başlıyor.")