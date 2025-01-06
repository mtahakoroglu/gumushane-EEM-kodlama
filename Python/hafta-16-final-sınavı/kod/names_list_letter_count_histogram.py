import matplotlib.pyplot as plt # en sonunda histogramı çizdirmek için
import numpy as np

def harfleri_say(isimler):
    harf_sayisi_listesi = [] # her bir isimdeki harf sayısını tutacak liste
    for isim in isimler:
        harf_sayisi_listesi.append(len(isim))
    return harf_sayisi_listesi

def yeni_liste(isimler, harfSayisi):
    yeni_isim_listesi = [] # ilgilendiğimiz sayıdaki harfe sahip isimlerin listesi
    for isim in isimler:
        if len(isim) == harfSayisi:
            yeni_isim_listesi.append(isim.title())
    return yeni_isim_listesi

isimler = ["ALİ", "nour", "tabarak", "derya", "patRICK",  
         "sefa", "can", "Serhat", "TaHa", "sude", 
         "melisa", "merT", "Deniz", "AHmeT", "mesut", 
         "melike", "zeynep", "cem", "merve", "ayşe"]

# Listeyi ve eleman sayısını ekrana basalım
print(f"İsim listesi: {isimler}")
print(f"isimler listesinde {len(isimler)} isim vardır.")

# flag ile listede harf_sayisi harfe sahip en az bir isim var mı kontrol edeceğiz
flag, harfSayisi = False, []
while True:
    # ask the user how many names consist of entered number of letters
    harfSayisi = int(input("Kaç harfli isimlerin sayısını öğrenmek istersiniz? "))
    # kullanıcının girdiği harf sayısına sahip en az bir isim var mı diye listeyi dolaş
    for isim in isimler:
        if len(isim) == harfSayisi:
            flag = True # en az bir isim bulunduğundan dolayı...
            break # ... isim listesi içinde arama işlemine son ver
    if flag: # listede harf_sayisi harfli en az bir isim bulunduysa döngüden çık
        break
    else:
        print(f"Listede {harfSayisi} harfli isim bulunmamaktadır. Tekrar deneyiniz.")

# isimler listesindeki isimlerin harf sayılarını tutan listeyi oluştur
harf_sayisi_listesi = harfleri_say(isimler)
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