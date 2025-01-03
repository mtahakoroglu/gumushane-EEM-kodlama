import matplotlib.pyplot as plt


def name_stats(names, start_letter):
    new_list = []
    for name in names:
        if name[0].lower() == start_letter:
            new_list.append(name)
    return len(new_list), new_list

names = ["ali", "burak", "atilla", "derya", "patrick",
         "sefa", "zeliha", "Serhat", "Ömer", "sude", 
         "melisa", "Mert", "Deniz", "demir", "mesut", 
         "alperen", "zeynep", "mehmet", "merve", "ayşe"]

print(f"İsim listesi {names}")
letter = input("Hangi harf ile başlayan isimlerin istatistiğine bakmak istersiniz? ")
n, new_list = name_stats(names, letter)
print(f"{letter} harfi ile başlayan isim sayısı = {n}")
print(f"{letter} harfi ile başlayan isimlerin listesi {new_list}.")

# İsimleri başlangıç harfine göre sayıp alfabetik olarak bar grafiğinde gösterelim
name_dict = {}
for name in names:
    if name[0].lower() in name_dict:
        name_dict[name[0].lower()] += 1
    else:
        name_dict[name[0].lower()] = 1
name_dict = dict(sorted(name_dict.items()))
plt.bar(name_dict.keys(), name_dict.values())
plt.xlabel("Harfler")
plt.ylabel("İsim Sayısı")
plt.title("İsimlerin Başlangıç Harfine Göre Sayısı")
plt.show()