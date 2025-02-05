import matplotlib.pyplot as plt

def name_stats(names, letter):
    new_list = [] # boş bir liste oluşturalım
    for name in names:
        if name.lower()[0] == letter.lower():
            new_list.append(name.title())
    return new_list

names = ["ALİ", "beren", "tabarak", "derya", "patRICK", "abdullah", 
         "sefa", "zeliha", "Serhat", "TaHa", "sude", "selen", 
         "melisa", "merT", "Deniz", "AHmeT", "mesut", "mehmet",
         "alpEREn", "zeynep", "mike", "merve", "ayşe", "fatma"]
print(f"İsim listesi {names}")
print(f"names isimli listede {len(names)} isim vardır.")
letter = input("Hangi harf ile başlayan isimlerin sayısını öğrenmek istersiniz? ")
new_list = name_stats(names, letter)
print(f"{letter} harfi ile başlayan isimler = {new_list}")
print(f"{letter} harfi ile başlayan isim sayısı = {len(new_list)}")

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
plt.xlabel("Harfler")
plt.ylabel("İsim Sayısı")
plt.title("İsimlerin Başlangıç Harfine Göre Sayısı")
plt.show()