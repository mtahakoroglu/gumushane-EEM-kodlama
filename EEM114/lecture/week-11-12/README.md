<h3>POPULER PYTHON KÜTÜPHANELERİNDE NUMPY KULLANIMI - OPENCV ÖRNEĞİ</h3>

<h4>Bir Matrisi Eşik Değerden Geçirerek Binary Hâle Getirmek</h4>

<p align="justify">Elemanları [0-255] aralığında birer tamsayı olan 5x8'lik rasgele bir A matrisi üretiniz (<b>numpy.random</b> sınıfından transfer ettiğiniz <b>randint()</b> fonksiyonu ile). Yine elemanları [0-255] aralığında birer tamsayı olan 5x8'lik rasgele bir B matrisi üretiniz (bu sefer <b>numpy.random</b> sınıfından <b>rand()</b> fonksiyonu ile). A ve B matrislerini veri tipi açısından hem standart <b>type()</b> fonksiyonuyla hem de <b>numpy</b> paketinden <b>dtype</b> özniteliğiyle kontrol ediniz. Ardından her iki matrisi de siyah-beyaz hale getiriniz (siyah 0 ile temsil edilirken beyaz 255 ile temsil edilmektedir).</a>

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


<p align="justify">Özellikle nümerik veriler (e.g., int, float) için <a href="https://6sense.com/tech/data-science-machine-learning">popüler Python kütüphanelerinin</a> (e.g., TensorFlow, PyTorch, OpenCV, Keras, Scikit-Learn) hepsi NumPy paketini/kütüphanesini (package/library) kullanmakta. Örnek olarak bir görüntü işleme (image processing), bilgisayarlı görü (computer vision), makine öğrenmesi (machine learning) ve derin öğrenme (deep learning) kütüphanesi olan OpenCV'de bir fotoğrafın bilgisayar hafızasında Python API'da hangi veri tipi olarak tutulduğuna bakalım. Bunun için Anaconda yüklemek ve Anaconda'da <b>opencv</b> isimli bir sanal ortam (virtual environment) oluşturup orada bir resmi okuyup ekranda görüntüleyen bir kod yazalım ve en sonunda yine <b>type()</b> komutuyla konsolda fotoğrafı tutan veri tipini görüntüleyelim. İlgili videoyu izlemek için tıklayınız.</p>