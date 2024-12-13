number = 41
while True:
    x = int(input("Bir tam sayı giriniz: "))
    if x == number:
        print("Tebrikler doğru tahmin ettiniz.")
        break
    elif x < number:
        print("Daha büyük bir sayı giriniz.")
    else:
        print("Daha küçük bir sayı giriniz.")