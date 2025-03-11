names = ['Willy', 'Arhan', 'Mustafa', 'Abdullah', 'Jesuno', 'Bonaventura', 
         'Manuel', 'Abdulrahim', 'Ziya', 'Rukiye', 'Taha']
print(f"names = {names}")
print(f"İsimler listesinde {len(names)} eleman vardır.")
# Arhan'ı listeden silmek istiyorum
names.remove(names[1])
print(f"names = {names}")
# listenin 3. elemanını silmek istiyorum
names.remove(names[2])
print(f"names = {names}")
# listenin son elemanını silmek istiyorum
names.remove(names[-1])
print(f"names = {names}")
# Abdulrahim'i de listeden ama bu sefer del komutuyla silelim
del names[-3]
print(f"names = {names}")
# Bonaventura'nın yerine Hande'yi koyalım
names[names.index("Bonaventura")] = "Hande"
print(f"names = {names}")
# pop() ile Jesuno'yu atalım
names.pop(2)
print(f"names = {names}")