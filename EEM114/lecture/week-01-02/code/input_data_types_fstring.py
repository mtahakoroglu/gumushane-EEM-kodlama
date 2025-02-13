name = input("İsminiz nedir? ")
age = int(input(f"Merhaba {name}! Kaç yaşındasın? "))
print(f"10 sene sonra {age+10} yaşında olacaksın.")
weight = float(input("Kaç kilosun {name}? "))
weightInt = round(weight)
print(f"Yuvarlak hesap {weightInt}kg diyebiliriz.")
height = int(input("Peki boyun (cm olarak) kaç? "))
# Burada kilo-boy oranına kabaca bakalım ve duruma göre ekrana mesaj yazalım
if height-100 > weightInt:
    print("Biraz kilo alsan iyi olur!")
elif height-100 == weightInt:
    print("Boyuna göre kilon iyi!")
else:
    print("Biraz kilo versen iyi olur!")
    
print(f"type(name) = {type(name)}")
print(f"type(age) = {type(age)}")
print(f"type(weight) = {type(weight)}")
print(f"type(height-100 > weightInt) = {type(height-100 > weightInt)}")

print(f"{name} {age} yaşında {weight}kg {height}cm boyunda birisidir.")