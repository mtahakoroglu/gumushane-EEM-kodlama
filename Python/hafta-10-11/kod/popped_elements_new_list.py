names = ["Ali", "berat", "Cindy", "davud", "SAFA",
         "Ece", "sefa", "Gizem", "Selin", "İsmail"]
print(f"names = {names}")
print(f"names isimli listede {len(names)} kişi vardır.")
# listeden baş harfi S ile başlayan isimleri listeden çıkaracağız
popped_names = []
i = 0
while i < len(names):
    if names[i][0].upper() == "S":
        popped_names.append(names.pop(i))
    else:
        i += 1
print(f"Çıkarılan isimler = {popped_names}")
print(f"İlk listenin son hâli = {names}")