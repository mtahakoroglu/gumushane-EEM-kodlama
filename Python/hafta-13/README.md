<h3>HAFTA 13: FONKSİYONLAR</h3>

<h4>Python Listelerinde Döngü, Koşullu İfade ve String Metotları Egzersizleri</h4>

<p align="justify">Aşağıda ders kitabından aldığımız <b>cars.py</b> kodunu bulabilirsiniz. İlgili video için <a href="https://www.youtube.com/watch?v=jaXPlEWvgxQ">tıklayınız</a>.</p>

<p align="justify"><b>cars.py</b></p>

```
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

<p align="justify">Aşağıda ders kitabından aldığımız <b>cars.py</b> kodundan hareketle kendi ürettiğimiz <b>names.py</b> kodunu bulabilirsiniz. İlgili video için <a href="https://www.youtube.com/watch?v=IgQNqG20otU">tıklayınız</a>.</p>

<p align="justify"><b>names.py</b></p>

```
names = ['Rukiye', 'Handenur', 'Abdullah', 'İbrahim', 'Rana']
for name in names:
    if name[0].lower() == 'r':
        print(name.upper())
    else:
        print(name.lower())
```

<h4>if - else if - else koşullu ifadeleri - Başka Bir Örnek</h4>

<p align="justify">Kitaptan koşullu ifadelerle ilgili bir başka örnek: <b>hayat.py</b> isimli kodun videosu için <a href="https://www.youtube.com/watch?v=SChaa65x1Lo&list=PLMoe16OQDeeCpsXqSpWs0LqOYUjlIu_jg&index=28">tıklayınız</a>.</p>

<p align="justify"><b>hayat.py</b></p>

```
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
```

<p align="justify">Kitaptan koşullu ifadelerle ilgili bir başka örnek: <b>stages_in_life.py</b> isimli kodun videosu için <a href="https://www.youtube.com/watch?v=tOWbycYozGk&list=PLMoe16OQDeeCpsXqSpWs0LqOYUjlIu_jg&index=29">tıklayınız</a>.</p>

<b>stages_in_life.py</b>

```
age = int(input("How old are you? "))
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")
```

<h4>Bir Çemberin Çevre ve Alanını Fonksiyon ile Bulma</h4>

<p align="justify">Bugüne kadar Python listeleri ve NumPy dizileri üzerinde döngü ile dolaşarak bir takım işlemler yaptık. Bu işlemleri kodun içinde yeri geldiğinde gerçekledik. Artık kendi fonksiyonlarımızı kendimiz yazarak bu işlemleri otomatik hâle getireceğiz. Burada çemberin çevresini ve alanını hesapladığımız kodda kendi fonksiyonumuzu yazmayı görürken bir sonraki kod olan bir matrisi eşik değerden geçirerek binary hâle getirme meselesinde fonksiyonların kıymetini anlayacağız.</p>

<p align="justify">Aşağıda verilen <b>circle_perimeter_area.py</b> kodunda bir çemberin çevresini ve alanını hesaplamayı kodun içinde görürken <b>circle_perimeter_area_function.py</b> isimli kodda ise bu işlemi fonksiyonla yapmayı göreceğiz.</p>
