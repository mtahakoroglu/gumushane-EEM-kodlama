COLOR = (255, 255, 255) # beyaz renk kodu
# bir döngü ile COLOR isimli TUPLE içindeki elemanları ekrana yazdıralım
for color in COLOR:
    print(color)
# başka bir döngü ile COLOR isimli TUPLE içindeki elemanları ekrana yazdıralım
for i in range(len(COLOR)):
    print(f"{i + 1}. eleman: {COLOR[i]}")
# COLOR isimli TUPLE'ın elemanlarını değiştirmeye çalışalım
# COLOR[0] = 0 # hata verecektir
# COLOR isimli TUPLE'ı yeniden tanımlayalım
COLOR = (0, 0, 0) # siyah renk kodu
print(f"COLOR = {COLOR}")
# üç farklı değişkeni aynı satırda atayalım
age, name, weight = 21, "Furkan", 70.3
print(f"age = {age}, name = {name}, weight = {weight}")
print(f"type(age) = {type(age)} type(name) = {type(name)} type(weight) = {type(weight)}")
print(f"type(age, name, weight) = {type((age, name, weight))}")