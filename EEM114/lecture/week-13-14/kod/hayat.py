age = int(input("Kaç yaşındasın? "))
if age < 2:
    print("Daha bebeksin.")
elif age < 4:
    print("Henüz yürümeye başladın.")
elif age < 13:
    print("Çocuksun.")
elif age < 20:
    print("Gençsin.")
elif age < 65:
    print("Yetişkinsin.")
else:
    print("Yaşlısın.")
    