names = ["Önder", "Furkan", "Sefa", "Safa", "Patrick", "Mahmoud", "Cindy"]
print(f"names = {names}") # isimler listesi
print(f"names[0:3] = {names[0:3]}") # ['Önder', 'Furkan', 'Sefa']
print(f"names[4:6] = {names[4:6]}") # ['Patrick', 'Mahmoud']
print(f"names[-2:] = {names[-2:]}") # ['Mahmoud', 'Cindy']
# Safa ile Patrick isimlerini yazdırmak istemiyoruz. Diğerlerini yazıralım.
print(f"names[:3] + names[5:] = {names[:3] + names[5:]}") # ['Önder', 'Furkan', 'Sefa', 'Mahmoud', 'Cindy']
# Sefa ile Patrick isimlerini yazdırmak istemiyoruz. Diğerlerini yazdıralım.
print(f"names[:2] + [names[3]] + names[-2:] = {names[:2] + [names[3]] + names[-2:]}") # ['Önder', 'Furkan', 'Safa', 'Mahmoud', 'Cindy']