<h3>HAFTA 13: KOŞULLU İFADELER TEKRAR ve FONKSİYONLARA GİRİŞ</h3>

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

<p align="justify">(Hayatın Aşamaları): Bir insanın hayatta hangi aşamada olduğunu belirten bir if-elif-else zinciri yazınız. Kullanıcıya yaşını sorarak kullanıcının girdiği değeri age değişkenine atayın ve daha sonra:</p>

<ul>
<li>Kişi 2 yaşından küçük ise bu kişinin bebek olduğunu belirten bir mesajı ekrana yazdırınız.</li>
<li>Kişi en az 2 yaşında ama 4 yaşından küçük ise bu kişinin yürümeye yeni başlayan bir çocuk olduğunu belirten bir mesajı ekrana yazdırınız.</li>
<li>Kişi en az 4 yaşında ama 13 yaşından küçük ise bu kişinin çocuk olduğunu belirten bir mesajı ekrana yazdırınız.</li>
<li>Kişi en az 13 yaşında ama 20 yaşından küçük ise bu kişinin ergen olduğunu belirten bir mesaj ekrana yazdırınız.</li>
<li>Kişi en az 20 yaşında ama 65 yaşından küçük ise bu kişinin yetişkin olduğunu belirten bir mesajı ekrana yazdırınız.</li>
<li>Kişi 65 yaş ve üzeri ise bu kişinin yaşlı olduğunu belirten bir mesajı ekrana yazınız.</li>
</ul>

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

<p align="justify">(Stages of Life): Write an if-elif-else chain that determines a person’s stage of life. Get the user’s age by asking him/her a related question in the console and assign the entered value to age variable and then:</p>

<ul>
<li>If the person is less than 2 years old, print a message that the person is a baby.</li>
<li>If the person is at least 2 years old but less than 4, print a message that the person is a toddler.</li>
<li>If the person is at least 4 years old but less than 13, print a message that the person is a kid.</li>
<li>If the person is at least 13 years old but less than 20, print a message that the person is a teenager.</li>
<li>If the person is at least 20 years old but less than 65, print a message that the person is an adult.</li>
<li>If the person is age 65 or older, print a message that the person is an elder.</li>
</ul>

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

<h4>Bir Çemberin Çevresini ve Alanını Fonksiyon ile Bulma</h4>

<p align="justify">Bugüne kadar Python listeleri ve NumPy dizileri üzerinde döngü ile dolaşarak bir takım işlemler yaptık. Bu işlemleri kodun içinde yeri geldiğinde gerçekledik. Artık kendi fonksiyonlarımızı kendimiz yazarak bu işlemleri otomatik hâle getireceğiz. Burada çemberin çevresini ve alanını hesapladığımız kodda kendi fonksiyonumuzu yazmayı görürken bir sonraki kod olan bir matrisi eşik değerden geçirerek binary hâle getirme meselesinde fonksiyonların niye bize gerektiğini tam mânâsıyla anlayacağız.</p>

<p align="justify">Aşağıda verilen <b>circle_perimeter_area.py</b> kodunda bir çemberin çevresini ve alanını hesaplamayı kodun içinde görürken <b>circle_perimeter_area_function.py</b> isimli kodda ise bu işlemi fonksiyonla yapmayı göreceğiz. İlgili video için <a href="https://www.youtube.com/watch?v=DovWv00Ctac&list=PLMoe16OQDeeCpsXqSpWs0LqOYUjlIu_jg&index=30">tıklayınız</a>.</p>

<b>circle_perimeter_area.py</b>

```
import numpy as np
r = float(input("Çemberin yarıçapını giriniz: "))
perimeter = 2*np.pi*r
area = np.pi*r**2
print(f"Yarıçapı {r} olan çemberin çevresi {perimeter:.2f}, alanı {area:.2f}'dir.")
```

<b>circle_perimeter_area_function.py</b>

```
import numpy as np

def circle_perimeter_area(radius):
    perimeter = 2 * np.pi * radius
    area = np.pi * radius ** 2
    return perimeter, area

r = float(input("Çemberin yarıçapını giriniz: "))
p, a = circle_perimeter_area(r)

print(f"Yarıçapı {r} olan çemberin çevresi {p:.2f}, alanı {a:.2f}'dir.")
```

<h4>Bir Matrisi Eşik Değerden Geçirerek Binary Hâle Getirmek</h4>

<p align="justify">Elemanları [0-255] aralığında birer tamsayı olan 5x8'lik rasgele bir A matrisi üretiniz (numpy.random sınıfından transfer ettiğiniz randint fonksiyonu ile). Yine elemanları [0-255] aralığında birer tamsayı olan 5x8'lik rasgele bir B matrisi üretiniz (numpy.random sınıfından rand fonksiyonu ile). A ve B matrislerini veri tipi açısından hem type() fonksiyonuyla hem de numpy paketinden <b>dtype()</b> fonksiyonuyla analiz ediniz. Ardından girişi bir matris ile bir skaler (eşik değeri) olan (iki girişli), çıkışı ise binary bir matris olan (eğer giriş matrisinin elemanları eşik değerinden düşükse o zaman çıkış matrisinde tekabül eden eleman 0, aksi takdirde 255) <b>matrix_threshold()</b> isimli fonkiyon yazarak her iki matrisi de siyah-beyaz hale getiriniz (siyah 0 ile temsil edilirken beyaz 255 ile temsil edilmektedir).</a>

<p align="justify">İlgili video için <a href="https://www.youtube.com/watch?v=lc80Qst1TGs&list=PLMoe16OQDeeCpsXqSpWs0LqOYUjlIu_jg&index=31">tıklayınız</a>.</a>

<b>matrix_thresholding.py</b>

```
from numpy.random import randint
from numpy.random import rand
import numpy as np

def matrix_threshold(M, threshold):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i,j] < threshold:
                M[i,j] = 0
            else:
                M[i,j] = 255
    return M

min_value, max_value = 0, 255
r, c = 5, 8
A = randint(min_value, max_value+1, (r,c))
B = np.round(255*rand(r,c))

print(f"A = {A}")
A_binary = matrix_threshold(A, 100)
print(f"A_binary = {A_binary}")
print(f"B = {B}")
B_binary = matrix_threshold(B, 50)
print(f"B_binary = {B_binary}")
print(f"A.dtype = {A.dtype}")
print(f"B.dtype = {B.dtype}")
```
