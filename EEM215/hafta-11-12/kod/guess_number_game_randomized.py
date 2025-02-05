# 0 ile 100 arasında (dâhili) rasgele bir sayı üretelim
from numpy.random import randint
minNumber, maxNumber = 0, 100
number = randint(minNumber, maxNumber+1)
while True:
    x = int(input("Bir tam sayı giriniz: "))
    if x == number:
        print("Tebrikler doğru tahmin ettiniz.")
        break
    elif x < number:
        print("Daha büyük bir sayı giriniz.")
    else:
        print("Daha küçük bir sayı giriniz.")