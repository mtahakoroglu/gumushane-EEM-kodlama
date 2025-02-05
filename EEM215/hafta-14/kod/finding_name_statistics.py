import matplotlib.pyplot as plt

def name_stats(names, letter):
    new_list = []
    for name in names:
        if name.lower()[0] == letter.lower():
            new_list.append(name.title())
    return new_list

names = ["ALİ", "burak", "tabarak", "derya", "patRICK", "abdullah", 
         "sefa", "zeliha", "Serhat", "TaHa", "sude", "selen", 
         "melisa", "merT", "Deniz", "AHmeT", "mesut", "mehmet",
         "alpEREn", "zeynep", "mehmet", "merve", "ayşe", "fatma"]

print(f"names = {names}")
print(f"names isimli listede {len(names)} isim vardır.")
letter = input("Hangi harf ile başlayan isimlerin istatistiğine bakmak istersiniz? ")
new_list = name_stats(names, letter)
print(f"{letter} harfi ile başlayan isimlerin sayısı = {len(new_list)}")
print(f"{letter} harfi ile başlayan isimler = {new_list}")

# İsimleri başlangıç harfine göre sayıp alfabetik olarak bar grafiğinde gösterelim
name_dict = {}
for name in names:
    if name.lower()[0] in name_dict:
        name_dict[name.lower()[0]] += 1
    else:
        name_dict[name.lower()[0]] = 1
name_dict = dict(sorted(name_dict.items()))
plt.bar(name_dict.keys(), name_dict.values(), color="lightgray", edgecolor="black")
plt.xlabel("Harfler")
plt.ylabel("İsim Sayısı")
plt.title("İsimlerin Başlangıç Harfine Göre Sayısı")
plt.tight_layout() # adjust the padding
plt.savefig("../isim_listesi_histogram.png", dpi=1200)
plt.show()
