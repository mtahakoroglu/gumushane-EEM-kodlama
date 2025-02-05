names = ['Çınay', 'Safa', 'Tabarak', 'Abdurrahman', 'Abdullah', 'Nour', 'Önder']
print(f"names = {names}")
del names[2] # 3. eleman olan Tabarak'i listeden çıkaralım
print(f"names = {names}")
names.remove('Nour') # Nour'u da listeden çıkaralım
print(f"names = {names}")
last_person = names.pop() # listenin son elemanını çıkaralım
print(f"Listenin sonunda {last_person} vardı. Onu da çıkardık.")
print(f"names = {names}")
# şimdi pop() metoduyla listenin istediğimiz bir konumundan bir eleman çıkaralım
second_person = names.pop(1) # 2. eleman olan Safa'yı listeden çıkaralım
print(f"İkinci sıradaki kişi olan {second_person} listeden çıkarıldı.")
print(f"names = {names}")
# for öngüsü ile listenin elemanlarını sırayla ekrana yazdıralım
for i in range(len(names)):
    print(f"{i + 1}. {names[i].upper()}")