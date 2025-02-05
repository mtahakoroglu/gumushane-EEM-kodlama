import matplotlib.pyplot as plt
'''Burada extract_names_list_starting_with_letter() isimli fonksiyonu, 
girişleri (yâni argümanları) names ve letter değişkenleri (isim listesi 
ve ilgilendiğimiz harf), çıkışı letter harfi ile başlayan isim listesi 
olacak biçimde tanımlayalım.'''
def extract_names_list_starting_with_letter(names, letter):
    new_list = [] # boş bir liste oluşturalım
    for name in names: # isimler listesinde dolaşalım
        if name.lower()[0] == letter.lower():
            new_list.append(name.title())
    return new_list
names = ["ALİ", "melek", "behZAt", "deren", "adem", "cem", 
         "ceyda", "zeliha", "Ceyhun", "TaHa", "sude", "selen", 
         "melisa", "merT", "Deniz", "AHmeT", "mesut", "mehmet",
         "alpEREn", "cindy", "zeynep", "merve", "ayşe", "fatma"]
print(f"İsim listesi {names}")
print(f"names isimli listede {len(names)} isim vardır.")
letter = input("Hangi harf ile başlayan isimlerin sayısını öğrenmek istersiniz? ")
# Fonksiyonu aşağıdaki gibi çağırıp son olarak istenen şeyleri ekrana basmalıyız.
new_list = extract_names_list_starting_with_letter(names, letter)
print(f"{letter} harfi ile başlayan isim sayısı = {len(new_list)}")
print(f"{letter} harfi ile başlayan isimler = {new_list}")

# names isimli listede yer alan isimleri ilk harfine göre histogramını çizdir
name_dict = {}
for name in names:
    first_letter = name[0].upper()
    if first_letter in name_dict:
        name_dict[first_letter] += 1
    else:
        name_dict[first_letter] = 1
sorted_name_dict = dict(sorted(name_dict.items()))

plt.bar(sorted_name_dict.keys(), sorted_name_dict.values(), color="lightgray", edgecolor="black")
plt.xlabel("Harfler", fontsize=14)
plt.ylabel("İsim Sayısı", fontsize=14)
plt.xticks(fontsize=14)  # X eksenindeki tick'lerin boyutunu ayarlayın
plt.yticks(fontsize=14)  # Y eksenindeki tick'lerin boyutunu ayarlayın
plt.title("İsimlerin Başlangıç Harfine Göre Sayısı", fontsize=14)
plt.grid(True, linestyle='--')
plt.tight_layout()
plt.savefig("names_list_starting_with_letter_histogram.png", dpi=1200)
plt.show()
