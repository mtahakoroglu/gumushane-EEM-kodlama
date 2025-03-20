# üç farklı değişkeni aynı satırda atayalım
age, name, weight = 20, "Arhan", 88.2
print(f"age = {age}, name = {name}, weight = {weight}")
# değişiklik yapalım
age, name, weight = 20, "Orhan", 88.2
print(f"age = {age}, name = {name}, weight = {weight}")
# TUPLE: demet manasına geliyor
COLOR = (255, 255, 255) # beyaz renk kodu
print(f"COLOR = {COLOR}   type(COLOR) = {type(COLOR)})")
# COLOR isimli TUPLE'ın elemanlarını değiştirmeye çalışalım
COLOR[0] = 0 # hata verecektir
# COLOR isimli TUPLE'ı yeniden tanımlayalım
COLOR = (0, 0, 0) # siyah renk kodu
print(f"COLOR = {COLOR}")