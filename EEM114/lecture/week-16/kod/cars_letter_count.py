cars = ['audi', 'bmw', 'subaru', 'toyota', 'mercedes', 'honda', 'ford', 'nissan']
# n harfli olan araba isimlerini büyük yaz, diğerlerini sadece ilk harf büyük yaz
n = 6
for car in cars:
    if len(car) == n:
        print(car.upper())
    else:
        print(car.title())