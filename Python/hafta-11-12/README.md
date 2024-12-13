<h3>NUMPY PAKETİ ile 1b-2b DİZİLER ve RASGELE SAYI ÜRETECİ</h3>

<h4>BİLGİSAYARA NUMPY YÜKLEME</h4>
<p align="justify">Bugüne kadar benzer veya ilişkili elemanlara bilgisayarın hafızasında ayrı ayrı değişkenlerle değil de tek bir değişken ismiyle erişmek istediğimizde Python listelerini kullanmıştık. Şimdi burada hızlıca <b>NumPy</b> paketini yükleyip Python listelerinde yaptığımız bir egzersizin aynısını bu sefer NumPy dizileri ve fonksiyonlarıyla gerçekleştireceğiz. İlk önce bilgisayarımıza NumPy paketini PowerShell (PS) konsolundan aşağıdaki gibi yükleyerek işe başlıyoruz.
</p>

```
pip install numpy
```

<p align="justify">Bilgisayarınızdaki PS terminali <b>Python Install Package</b> manasına gelen <b>pip</b> komutunu tanımıyorsa o zaman <a href="https://www.python.org/">python.org</a> sitesinden Python yüklerken "PATH'e ekle" seçeneğini seçmemişsiniz demektir. Bu hata ile ilgili video için <a href="https://www.youtube.com/watch?v=xHAjOgX6vOQ">tıklayınız</a>. Çözüm için "PATH'e ekle" seçeneğini seçerek Python'ı tekrar yüklenemeniz gerekmekte. Başka çözümler de var ama sizler için bu en kolay ve kısa olanı.</p>

<h4>NUMPY ile 1b DİZİLER</h4>

<p align="justify">Daha önce Python listelerinde yaptığımız şekilde, bize verilen bir dizinin değişik yerlerine elemanla ekleyelim, değişik yerlerinden elemanları çıkaralım/silelim. Bu arada PowerShell'de hızlıca <b>numbers</b> isimli değişkenin veri tipine <b>type(numbers)</b> fonksiyonu ile bakalım.</p>

<b>list_methods_exercise.py</b>

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

<p align="justify">Aşağıda bize NumPy'da 2b bir dizi verilmekte. Biz bu yapıya doğrusal cebirde <b>matris</b> diyoruz. Resimde gösterilen elemanlara, vektörlere ve alt matrislere aşağıdaki kodda verildiği gibi erişebiliriz. İlgili videoyu izlemek için tıklayınız.</p>

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

<h4>POPULER PYTHON KÜTÜPHANELERİNDE NUMPY KULLANIMI</h4>
<p align="justify">Özellikle nümerik veriler (e.g., int, float) için <a href="https://6sense.com/tech/data-science-machine-learning">popüler Python kütüphanelerinin</a> (e.g., TensorFlow, PyTorch, OpenCV, Keras, Scikit-Learn) hepsi NumPy paketini/kütüphanesini (package/library) kullanmakta. Örnek olarak bir görüntü işleme (image processing), bilgisayarlı görü (computer vision), makine öğrenmesi (machine learning) ve derin öğrenme (deep learning) kütüphanesi olan OpenCV'de bir fotoğrafın bilgisayar hafızasında Python API'da hangi veri tipi olarak tutulduğuna bakalım. Bunun için Anaconda yüklemek ve Anaconda'da <b>opencv</b> isimli bir sanal ortam (virtual environment) oluşturup orada bir resmi okuyup ekranda görüntüleyen bir kod yazalım ve en sonunda yine <b>type()</b> komutuyla konsolda fotoğrafı tutan veri tipini görüntüleyelim. İlgili videoyu izlemek için tıklayınız.</p>
