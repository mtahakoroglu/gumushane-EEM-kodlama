age = int(input("Yaşın kaç? "))
if age < 2:
    print("Bebeksin.")
elif age < 4:
    print("Yürümeye başlayan küçük bir çocuksun.")
elif age < 13:
    print("Çocuksun.")
elif age < 20:
    print("Gençsin.")
elif age < 65:
    print("Yetişkinsin.")
else:
    print("Yaşlısın.")