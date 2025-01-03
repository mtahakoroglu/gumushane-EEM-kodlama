<h3>HAFTA 14: FONKSİYONLAR ve MATPLOTLİB KULLANIMI</h3>

<p align="justify">Geçtiğimiz hafta kendi fonksiyonlarımızı (user-defined function) yazmaya başladık. Bu hafta fonksiyonlar konusunda egzersizlerle devam ederken <b>matplotlib</b> paketi ile grafik (histogram) çizdirme ile devam edeceğiz. Grafik çizdirmek için kullanacağımız <b>matplotlib</b> isimli paketi kullanırken tamamen <b>GitHub Copilot</b> asistanından yardım alacağız.</p>

<p align="justify">EEM 217 Olasılık Kuramı dersinde sınıf yaş dağılımı sorusunda <b>matplotlib</b> ile histogram çizdirmiştik.</p>

<b>student_age_histogram.py</b>

```
from numpy.random import randint
import matplotlib.pyplot as plt
import numpy as np

def bilgi_olaylar_ihtimaller(ages, n):
    '''Bir sınıfta yer alan öğrencilerin yaşlarıyla ilgili çizdirilen histogramda tanımlanan olayların (events) olasılıklarının simülasyonla bulunması ve ekrana yazdırılması'''
    print(f"A: Öğrencinin 21 yaşından büyük olması --> P(A): {sum(ages > 21)}/{n} = {sum(ages > 21) / n}")
    print(f"B: Öğrencinin 20 yaşında veya daha küçük olması --> P(B): {sum(ages <= 20)}/{n} = ", sum(ages <= 20) / n)
    print(f"C: Öğrencinin 20 yaşından daha küçük veya 21 yaşından daha büyük olması --> P(C): {sum(ages < 20) + sum(ages > 21)}/{n} = {sum((ages < 20) | (ages > 21)) / n}")
    print(f"D: Öğrencinin 20 yaşında olması --> P(D): {sum(ages == 20)}/{n} = {sum(ages == 20) / n}")
    print(f"E: Öğrencinin 18 yaşında olması --> P(E): {sum(ages == 18)}/{n} = {sum(ages == 18) / n}")
    print(f"F: Öğrencinin 20 yaşından küçük olması --> P(F): {sum(ages < 20)}/{numberOfStudents} = {sum(ages < 20) / numberOfStudents}")
    print(f"E|F: 20 yaşından küçük olan bir öğrencinin 18 yaşında olması --> P(E|F): {sum(ages == 18)}/{sum(ages < 20)} = {sum(ages == 18)/sum(ages < 20)}")
    print(f"F|B: 20 yaşında veya daha küçük olan bir öğrencinin 20 yaşından küçük olması --> P(F|B): {sum(ages < 20)}/{sum(ages <= 20)} = {sum(ages < 20) / sum(ages <= 20)}")

numberOfStudents = 100 # öğrenci sayısı
minAge, maxAge = 18, 23 # yaş aralığı
ages = randint(minAge, maxAge+1, numberOfStudents) # rastgele yaşlar (tekdüze dağılım - uniform distribution)
# olaylar hakkında bilgi veren, ihtimalleri hesaplayan ve ekrana yazdıran fonksiyonu çağır
bilgi_olaylar_ihtimaller(ages, numberOfStudents)
# ages dizisinde yer alan yaşları histogramda göster
counts, bins, patches = plt.hist(
    ages,
    bins=np.arange(minAge - 0.5, maxAge + 0.5 + 1, 1),
    edgecolor='black',
    color='lightgray'
)
for i, patch in enumerate(patches):
    x = patch.get_x() + patch.get_width() / 2
    y = patch.get_height()
    plt.text(x, y, str(int(counts[i])), ha='center', va='bottom', fontsize=12)
plt.title('Öğrenci Yaş Histogramı'); plt.xlabel('Yaş'); plt.ylabel('Öğrenci Sayısı')
plt.show()
```

<p align="justify">Burada örnek bir sınav sorusu çözelim. İlgili video için <a href="youtube.com">tıklayınız.</a>

<p align="jsutify">Aşağıda bir isim listesi verilmiştir.</p>

```
names = ["ali", "burak", "atilla", "derya", "patrick",
         "sefa", "zeliha", "Serhat", "Ömer", "sude", 
         "melisa", "Mert", "Deniz", "demir", "mesut", 
         "alperen", "zeynep", "mehmet", "merve", "ayşe"]
```

<p align="justify">Kodun devamında ilk önce bu listeyi ekrana basalım.</p>

```
print(f"İsim listesi {names}")
```

<p align="justify">Ardından kullanıcıya bir soru soralım.

```
letter = input("Hangi harf ile başlayan isimlerin istatistiğine bakmak istersiniz? ")
```

<p align="justify">Burada <b>name_stats()</b> isimli bir fonksiyon tanımlayınız. Bu fonksiyona giriş olarak (yâni argüman olarak) <b>names</b> ve <b>letter</b> değişkenlerini (isim listesini ve ilgilendiğimiz harfi) veriniz. Çıkış olarak <b>name_stats()</b> fonksiyonu bize letter harfi ile başlayan isim sayısını ve bu harfle başlayan isim listesini döndürmeli. Fonksiyonu aşağıdaki gibi çağırıp son olarak da döndürülen değerleri ekrana basmalıyız.</p>

```
n, new_list = name_stats(names, letter)
print(f"{letter} harfi ile başlayan isim sayısı = {n}")
print(f"{letter} harfi ile başlayan isimlerin listesi {new_list}.")
```

<p align="justify">
Soru – devam (5 Puan) Grafik çizdirmede kullanacağımız <b>matplotlib</b> paketiyle <b>GitHub Copilot</b>'ın asistanlığında aşağıdaki yorumu koda ekleyerek <b>names</b> isimli listenin histogramını çizdiriniz.</p>

```
# İsimleri başlangıç harfine göre sayıp alfabetik olarak bar grafiğinde gösterelim
```

<img src="isim_listesi_histogram.png" alt="isim listesi histogram" width=500 height=auto>