<h3>ÖRNEK SINAV SORULARI</h3>

<p align="justify">İlgili video için <a href="https://www.youtube.com/watch?v=WPa5DRVCbe8">tıklayınız</a>.</p>

<b>cars_letter_count.py</b>

```
cars = ['audi', 'bmw', 'subaru', 'toyota', 'mercedes', 'honda', 'ford', 'nissan']
# n harfli olan araba isimlerini büyük yaz, diğerlerini sadece ilk harf büyük yaz
n = 6
for car in cars:
    if len(car) == n:
        print(car.upper())
    else:
        print(car.title())
```

<b>cars_modulo.py</b>

```
cars = ['audi', 'bmw', 'subaru', 'toyota', 'mercedes', 'honda', 'ford', 'nissan']
# araba ismi çift index'te ise hepsi büyük harf yaz, yoksa ilk harf büyük yaz
for i in range(len(cars)):
    if i % 2 == 0:
        print(cars[i].upper())
    else:
        print(cars[i].title())
```

<p align="justify">Yukarıdaki iki sorunun birleşimi olan örnek bir final sınav sorusu için <a href="https://www.youtube.com/watch?v=Rpr25ZZvdfU">tıklayınız</a>.</p>

<b>cars_final_exam.py</b>

```
cars = ['audi', 'bmw', 'subaru', 'toyota', 'renault', 'honda', 'ford', 'nissan', 'chevrolet', 'hyundai', 'kia', 'volkswagen', 'peugeot', 'fiat', 'mercedes']
n = 7 # harf sayısı
for i in range(len(cars)):
    if i % 4 == 0 and len(cars[i]) == n:
        print(cars[i].upper()) # şartları sağlayan araba isimlerini yazdır
```