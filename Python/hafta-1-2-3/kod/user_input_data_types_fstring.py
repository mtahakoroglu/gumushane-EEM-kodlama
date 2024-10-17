name = input("Kişinin ismi ne? ")
age = int(input(f"{name} isimli kişinin yaşı kaç? "))
weight = float(input(f"{name} isimli kişi kaç kg? "))
x, year, chernobylYear = 5, 2024, 1986
birthYear = year - age
print(f"{name} {birthYear} senesinde doğmuştur.")
print(f"{name} eğer {x}kg daha alırsa {weight+x}kg olacaktır.")
if chernobylYear > birthYear:
    print(f"{name} Chernobyl faciasından önce doğmuştur.")
elif chernobylYear == birthYear:
    print(f"{name} Chernobyl faciasıyla aynı senede doğmuştur.")
else:
    print(f"{name} Chernobyl faciasından sonra doğmuştur.")
##################### Printing Data Types ######################
print(f"type(name) = {type(name)}")
print(f"type(age) = {type(age)}")
print(f"type(weight) = {type(weight)}")
print(f"type(chernobylYear > birthYear) = {type(chernobylYear > birthYear)}")