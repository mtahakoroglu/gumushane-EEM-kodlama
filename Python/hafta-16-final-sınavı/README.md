<h3>HAFTA 16: FONKSİYONLAR ve MATPLOTLIB KULLANIMI - ÖRNEK FİNAL SINAVI SORUSU</h3>

<p align="justify">Örnek bir sınav sorusu çözelim. İlgili video için <a href="https://www.youtube.com/watch?v=1dqgCfbsiUg">tıklayınız.</a>

<p align="justify">Aşağıda bir isim listesi oluşturulmuştur.</p>

```
names = ["ALİ", "_________", "tabarak", "derya", "patRICK", "abdullah", 
         "sefa", "zeliha", "Serhat", "TaHa", "sude", "selen", 
         "melisa", "merT", "Deniz", "AHmeT", "mesut", "mehmet",
         "alpEREn", "zeynep", "________", "merve", "ayşe", "fatma"]
```

```
type(names)
type(names[0])
```

Kodun devamında bu listeyi ve eleman sayısını ekrana basalım ve kullanıcıya bir soru soralım.
print(___"İsim listesi __________")
print(___"names isimli listede {_________} isim vardır.")
letter=_______("Hangi harf ile başlayan isimlerin sayısını öğrenmek istersiniz? ")


<p align="justify">Burada <b>name_stats()</b> isimli bir fonksiyon tanımlayınız. Bu fonksiyona giriş olarak (yâni argüman olarak) <b>names</b> ve <b>letter</b> değişkenlerini (isim listesini ve ilgilendiğimiz harfi) veriniz. Çıkış olarak <b>name_stats()</b> fonksiyonu bize <b>letter</b> harfi ile başlayan isim sayısını ve bu harfle başlayan isim listesini döndürmeli. Fonksiyonu aşağıdaki gibi çağırıp son olarak da döndürülen değerleri ekrana basmalıyız.</p>

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

<img src="names_list_letter_count_histogram.png" alt="isim listesi harf sayısına göre histogram" width=500 height=auto>