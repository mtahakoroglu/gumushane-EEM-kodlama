names = ["Ali", "berat", "Cindy", "davud", "SAFA",
         "Ece", "sefa", "Gizem", "Selin", "İsmail"]
print(f"names = {names}")
print(f"names isimli listede {len(names)} kişi vardır.")
# listeden 's' ile başlayan isimleri silelim
popped_elements = []
i = 0
# while döngüsü ile yapalım
while i < len(names):
    if names[i].lower()[0] == "s":
        popped_elements.append(names.pop(i))
    else:
        i += 1
print(f"Listenin son hâli {names}")
print(f"Silinen isimler {popped_elements}")