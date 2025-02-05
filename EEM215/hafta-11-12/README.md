<h3>HAFTA 11-12: NUMPY PAKETİ ile 1b-2b DİZİLER ve RASGELE SAYI ÜRETECİ</h3>

<h4>BİLGİSAYARA NUMPY YÜKLEME</h4>
<p align="justify">Bugüne kadar benzer veya ilişkili elemanlara bilgisayarın hafızasında ayrı ayrı değişkenlerle değil de tek bir değişken ismiyle erişmek istediğimizde Python listelerini kullanmıştık. Şimdi burada hızlıca <b>NumPy</b> paketini yükleyip Python listelerinde yaptığımız bir egzersizin aynısını bu sefer NumPy dizileri ve fonksiyonlarıyla gerçekleştireceğiz. İlk önce bilgisayarımıza NumPy paketini PowerShell (PS) konsolundan aşağıdaki gibi yükleyerek işe başlıyoruz.
</p>

```
pip install numpy
```

<p align="justify">Bilgisayarınızdaki PS terminali <b>Python Install Package</b> manasına gelen <b>pip</b> komutunu tanımıyorsa o zaman <a href="https://www.python.org/">python.org</a> sitesinden Python yüklerken "PATH'e ekle" seçeneğini seçmemişsiniz demektir. Bu hata ile ilgili video için <a href="https://www.youtube.com/watch?v=xHAjOgX6vOQ">tıklayınız</a>. Çözüm için "PATH'e ekle" seçeneğini seçerek Python'ı tekrar yüklenemeniz gerekmekte. Başka çözümler de var ama sizler için bu en kolay ve kısa olanı.</p>

<h4>NUMPY ile 1b DİZİLER</h4>

<p align="justify">Daha önce Python listelerinde yaptığımız şekilde, verilen bir dizinin değişik yerlerine elemanla ekleyelim, değişik yerlerinden elemanları çıkaralım/silelim. Bu arada PowerShell'de hızlıca <b>numbers</b> isimli değişkenin veri tipine <b>type(numbers)</b> fonksiyonu ile bakalım. İlgili videoyu izlemek için aşağıdaki NumPy logosu resmine tıklayınız.</p>

<a href="https://www.youtube.com/watch?v=Ntocj4vgDoI"><img src="döküman/NumPy.png" alt="numpy-1d_array" width=500 height=auto></a>

<b>numpy_1d_array.py</b>

```
import numpy as np
numbers = np.array([7, 12, -3, 4, -5])
print(f"numbers = {numbers}")
# listenin sonuna 16 sayısını ekleyelim
numbers = np.append(numbers, 16)
print(f"numbers = {numbers}")
# listenin sonuna 2 ekleyelim
numbers = np.append(numbers, 2)
print(f"numbers = {numbers}")
# listenin başına 9 ekleyelim
numbers = np.insert(numbers, 0, 9)
print(f"numbers = {numbers}")
# listenin başından ikinci sıraya 5 ekleyelim
numbers = np.insert(numbers, 1, 5)
print(f"numbers = {numbers}")
# listenin başından üçüncü elemanı silelim
numbers = np.delete(numbers, 2)
print(f"numbers = {numbers}")
```

<h4>NUMPY ile 2b DİZİLER</h4>

<p align="justify">Aşağıda bize NumPy'da 2b bir dizi verilmekte. Biz bu yapıya doğrusal cebirde <b>matris</b> diyoruz. Resimde gösterilen elemanlara, vektörlere ve alt matrislere aşağıdaki kodda verildiği gibi erişebiliriz. İlgili videoyu izlemek için aşağıdaki matris resmine tıklayınız.</p>

<img src="döküman/numpy_2d_array.png" alt="numpy-2d-array" width=400 height=auto>

<b>numpy_2d_array.py</b>

```
import numpy as np

A = np.array([[-3, 5, -4, -2, 1, 5, -2, 0, -3, 15],
            [1, 11, 12, 9, 14, 4, -3, 5, 12, 7],
            [6, -2, 14, -4, -5, 8, 5, 9, 0, 4],
            [14, 3, 9, 1, 4, 9, 14, 13, 11, 2],
            [14, 13, 10, -4, 3, 10, 2, 14, 0, 12],
            [-2, 11, 10, -3, 10, 1, 7, 6, 14, 7],
            [14, 14, 3, 11, 11, 9, -1, -2, 2, 6],
            [14, 8, 8, 9, -1, 8, 10, -2, -1, 13]])

print(f"A = {A}")

a = A[-2,1]; print(f"a = {a}")
b = A[:,5]; print(f"b = {b}")
c = A[4,-4:]; print(f"c = {c}")
d = A[-3:,-2]; print(f"d = {d}")
e = A[0:2,-3:]; print(f"e = {e}")
f = A[-3:,3:5]; print(f"f = {f}")
g = A[2:4,:]; print(f"g = {g}")
```

<h4>FOR DÖNGÜSÜ range() KULLANIMI - ÖRNEK 1 ve 2</h4>

<p align="justify">Örnek 1 video için <a href="https://www.youtube.com/watch?v=ZXJMM6FDzYQ">tıklayınız</a>.</p>

```
start, stop, T = 2, 50, 4
for i in range(start, stop+1, T):
    print(i, end=" ")
```

<p align="justify">Örnek 2 video için <a href="https://www.youtube.com/watch?v=Xr9DCgQuCXI">tıklayınız</a>.</p>

```
for k in range(1,10,2): # 1-3-5-7-9
    print(3*k-1, end=" ") # 2-8-14-20-26
```

<h4>IF - ELIF - ELSE KOŞULLU İFADELER</h4>

<p align="justify">İçerisinde VE ve VEYA mantık kapılarını (AND and OR logic gates) tekrar ettiğimiz koşullu ifade örnek kodunun çıktısını görmek için <a href="https://www.youtube.com/watch?v=BCUrIYDbK4g">tıklayınız</a>.</p>

```
flag1, flag2 = False, True
if flag1:
    print("Merhaba!")
elif flag1 and True:
    print("Hola!")
elif flag1 or not flag2:
    print("Hello!")
elif not flag2:
    print("Güle güle dostum.")
elif not flag1 and flag2:
    print("Adios amigo.")
else:
    print("Good bye dude.")
```

<p align="justify">Tahmin etmek istediğimiz bir sayı var. Kullanıcı girişle bu sayıyı tahmin etmeye çalışıyor. İlgili videoyu izlemek için <a href="https://www.youtube.com/watch?v=9zjA759wick">tıklayınız</a>.</p>

```
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
```

<p align="justify">Tahmin etmek istediğimiz sayı bu sefer bilgisayara tarafından Python'da numpy paketi ile rasgele belirleniyor. Kullanıcı girişle bu sayıyı tahmin etmeye çalışıyor. İlgili videoyu izlemek için <a href="https://www.youtube.com/watch?v=OnmxA-plIaA">tıklayınız</a>.</p>

```
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
```

<h4>NUMPY ile RASGELE MATRİS OLUŞTURMA</h4>

<p>İlgili video için <a href="https://www.youtube.com/watch?v=pQPnR2zRSS0">tıklayınız</a>.</p>

```
import numpy as np
from numpy.random import randint
r, c = 3, 6 # row, column
A = randint(-25,51,(r,c))
print(A)
B = np.array([[2, 8, 4], [-5, 6, 12], [7, 3, -15]])
print(B)
```

<h4>POPULER PYTHON KÜTÜPHANELERİNDE NUMPY KULLANIMI</h4>
<p align="justify">Özellikle nümerik veriler (e.g., int, float) için <a href="https://6sense.com/tech/data-science-machine-learning">popüler Python kütüphanelerinin</a> (e.g., TensorFlow, PyTorch, OpenCV, Keras, Scikit-Learn) hepsi NumPy paketini/kütüphanesini (package/library) kullanmakta. Örnek olarak bir görüntü işleme (image processing), bilgisayarlı görü (computer vision), makine öğrenmesi (machine learning) ve derin öğrenme (deep learning) kütüphanesi olan OpenCV'de bir fotoğrafın bilgisayar hafızasında Python API'da hangi veri tipi olarak tutulduğuna bakalım. Bunun için Anaconda yüklemek ve Anaconda'da <b>opencv</b> isimli bir sanal ortam (virtual environment) oluşturup orada bir resmi okuyup ekranda görüntüleyen bir kod yazalım ve en sonunda yine <b>type()</b> komutuyla konsolda fotoğrafı tutan veri tipini görüntüleyelim. İlgili videoyu izlemek için tıklayınız.</p>
