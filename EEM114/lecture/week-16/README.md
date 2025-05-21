<h3>ÖRNEK SINAV SORULARI</h3>

<p align="justify">İlgili video için <a href="https://www.youtube.com">tıklayınız</a>.</a>

<b>print_car_names_modulo.py</b>

```
cars = ['audi', 'bmw', 'subaru', 'toyota', 'honda', 'ford', 'chevrolet', 'nissan']
for i in range(len(cars)):
    if i % 2 == 0:
        print(cars[i].upper())
    else:
        print(cars[i].title())
```

<p align="justify">İlgili video için <a href="https://www.youtube.com">tıklayınız</a>.</a>

<b>print_car_names_wrt_letter_count.py</b>

```
cars = ['audi', 'bmw', 'subaru', 'toyota', 'honda', 'ford', 'chevrolet', 'nissan']
# n harfli araba isimlerini büyük harfle, diğerlerinin sadece baş harfini büyük yaparak yazdırın
n = 6
for car in cars:
    if len(car) == n:
        print(car.upper())
    else:
        print(car.title())
```