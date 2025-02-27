names = ["Arhan", "mustafa", "aBdULLah", "JESUNO", 
         "bonaventurA", "AbdulRahim", "ziYA", "Umut",
         "eray", "ibo"]
print(names)
# liste metotları kullarak isimleri değişik formlarda ekrana basalım
print("İlk harfler büyük diğerleri küçük")
for name in names:
    print(name.title(), end=" ")
print("\nİsimlerdeki harflerin tamamı büyük") # \n bir alt satıra geçer
for name in names:
    print(name.upper(), end=" ")
print("\nİsimlerdeki harflerin tamamı küçük")
for name in names:
    print(name.lower(), end=" ")
# kitapta rstrip(), lstrip(), strip() metotları da kullanılmış
name = "     Arhan"
print(f"\nname = {name}    name.lstrip() = {name.lstrip()}")
name = "Arhan     "
print(f"name = {name}    name.rstrip() = {name.rstrip()}")
name = "    Arhan    "
print(f"name = {name}    name.strip() = {name.strip()}")