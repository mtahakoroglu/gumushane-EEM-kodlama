names = ["Arhan", "Mustafa", "Abdullah", "Jesuno", "Bonaventura", "Abdulrahim", "Ziya"]
ages = [21, 21, 20, 19, 22, 21, 19]
weight = [91.1, 64.2, 85.3, 79.6, 80.4, 65.7, 69.4]
attendance = [True, True, True, False, True, False, True]
# sınıfta yer alan kişilerin bilgilerini mânâlı bir cümle ile konsola yazdıralım
for i in range(len(names)):
    if attendance[i]:
        print(f"{names[i]}, {ages[i]} yaşında, {weight[i]}kg ağırlığında birisidir.")
    else:
        print(f"{names[i]} bugün derste yoktur.")