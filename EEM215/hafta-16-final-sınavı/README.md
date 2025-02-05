<h3>HAFTA 16: FONKSİYONLAR ve MATPLOTLIB KULLANIMI - ÖRNEK FİNAL SINAVI SORUSU</h3>

<p align="justify">Örnek bir sınav sorusu çözelim. İlgili video için <a href="https://www.youtube.com/watch?v=1dqgCfbsiUg">tıklayınız.</a>

```
import matplotlib.pyplot as plt # en sonunda histogram çizdirmek için gereken paket
import numpy as np

def harfleri_say(isimler): # giriş: isim listesi
    harf_sayisi_listesi = [] # her bir isimdeki harf sayısını tutacak liste
    for isim in isimler:
        harf_sayisi_listesi.append(len(isim)) # listeye isim uzunluğunu ekle
    return harf_sayisi_listesi # çıkış: harf sayısı listesi

def yeni_liste(isimler, harfSayisi): # girişler: isim listesi ve harf sayısı
    yeni_isim_listesi = [] # ilgilendiğimiz sayıdaki harfe sahip isimlerin listesi
    for isim in isimler:
        if len(isim) == harfSayisi: # eğer isim uzunluğu harfSayisi’na eşitse …
            yeni_isim_listesi.append(isim.title()) # … ismi listeye ekle
    return yeni_isim_listesi # çıkış: harfSayisi harfe sahip isim listesi

# isim listesinde boş olan yerlere uygun isimler yazınız
# yandaki histogramı sağlayacak bütün isimler olabilir
isimler = ["ALİ", "nour", "cem", "derya", "patRICK",
         "sefa", "can", "Serhat", "TaHa", "sude",
         "tabarak", "merT", "Deniz", "AHmeT", "mesut",
         "melike", "zeynep", "melisa", "merve", "ayşe"]

print(f"İsim listesi: {isimler}")
print(f"isimler listesinde {len(isimler)} isim vardır.")
# isimler listesindeki isimlerin harf sayılarını tutan listeyi oluştur
harf_sayisi_listesi = harfleri_say(isimler)

# flag ile listede harfSayisi harfe sahip en az bir isim var mı kontrol edeceğiz
flag, harfSayisi = False, []
while True: # sonsuz döngüye gir – burada Boolean bir ifade kullanılacak
   # kullanıcıya kaç harfli isim sayısını öğrenmek istediğini soralım
   harfSayisi=int(input("Kaç harfli isimlerin sayısını öğrenmek istersiniz? "))
   # kullanıcının girdiği harf sayısına sahip en az bir isim var mı diye listeyi dolaş
   for isim in isimler:
      if len(isim) == harfSayisi: # en az bir ismin harf sayısı harfSayisi’na eşitse…
         flag = True # … değişkene öbür Boolean değeri ata ve …
         break # … döngüyü kırarak isim listesi içinde dolaşmayı sonlandır
   if flag: # listede harfSayisi harfli en az bir isim bulunduysa …
      break # … döngüden çık
   else:
      print(f"Listede {harfSayisi} harfli isim bulunmamaktadır. Tekrar deneyiniz.")

print(f"İsimlerin harf sayıları: {harf_sayisi_listesi}")
# ilgilendiğimiz sayıdaki harfe sahip listeyi oluştur
yeni_isim_listesi = yeni_liste(isimler, harfSayisi)
# ilgilendiğimiz sayıdaki harfe sahip isimleri ekrana yazdır
print(f"{harfSayisi} harfli isimler: {yeni_isim_listesi}")
print(f"{harfSayisi} harfli isimlerin sayısı: {len(yeni_isim_listesi)}")

# histogramı çiz
plt.hist(harf_sayisi_listesi, 
         bins=np.arange(min(harf_sayisi_listesi)-0.5, max(harf_sayisi_listesi)+1+0.5, 1), 
         color="lightgray", edgecolor="black")
plt.xlabel("Harf Sayısı")
plt.ylabel("İsim Sayısı")
plt.title("İsimlerin Harf Sayıları Histogramı")
plt.tight_layout() # figürü ekrana tam sığdır
# x ekseninde xtick'leri 1'er artacak şekilde ayarla
plt.xticks(np.arange(min(harf_sayisi_listesi), max(harf_sayisi_listesi)+1, 1))
# grid çizgilerini ekle
plt.grid(True, linestyle='--')
plt.xlim(min(harf_sayisi_listesi)-0.5, max(harf_sayisi_listesi)+0.5)
plt.savefig("names_list_letter_count_histogram.png", dpi=600)
plt.show()
```
