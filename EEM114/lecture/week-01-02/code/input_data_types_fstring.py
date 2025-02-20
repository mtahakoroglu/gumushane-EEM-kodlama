name = input("İsminiz nedir? ")
age = int(input(f"Merhaba {name}! Kaç yaşındasın? "))
print(f"10 sene sonra {age+10} yaşında olacaksın.")
weight = int(input("Kaç kilosun {name}? "))
height = int(input("Peki boyun (cm olarak) kaç {name}? "))
# Burada kilo-boy oranına kabaca bakalım ve duruma göre ekrana mesaj yazalım
if height-100 > weight:
    print("Biraz kilo alsan iyi olur!")
elif height-100 == weight:
    print("Boyuna göre kilon iyi!")
else:
    print("Biraz kilo versen iyi olur!")
    
print(f"type(name) = {type(name)}")
print(f"type(age) = {type(age)}")
print(f"type(weight) = {type(weight)}")
print(f"type(height-100 > weight) = {type(height-100 > weight)}")

print(f"{name} {age} yaşında {weight}kg {height}cm boyunda birisidir.")