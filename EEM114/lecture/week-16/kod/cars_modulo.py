cars = ['audi', 'bmw', 'subaru', 'toyota', 'mercedes', 'honda', 'ford', 'nissan']
# araba ismi çift index'te ise hepsi büyük harf yaz, yoksa ilk harf büyük yaz
for i in range(len(cars)):
    if i % 2 == 0:
        print(cars[i].upper())
    else:
        print(cars[i].title())