names = ["Önder", "Furkan", "Sefa", "Safa", "Patrick", "Mahmoud", "Cindy"]
ages = [20, 21, 21, 20, 23, 25, 24]
weight = [73.6, 75.2, 64.1, 67.9, 71.1, 68.1, 50.3]
attendance = [True, True, True, True, False, True, True]
# for döngüsü ile listedeki öğrencilerin isimlerini, yaşlarını, kilolarını ve devamsızlık durumlarını ekrana yazdıralım
for i in range(len(names)):
    if attendance[i]:
        print(f"{names[i]} {ages[i]} yaşında olup {weight[i]} kg ağırlığındadır.")
    else:
        print(f"{names[i]} bugün sınıfta yoktur.")