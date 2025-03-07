<h3>LİSTELERLE ÇALIŞMA (WORKING w/ LISTS)</h3>

<h4>KARIŞIK LİSTE</h4>
<p align="justify">Şu ana kadar (3. ve 4. haftalarda) elemanları string, integer, float veya bool veri tipi olan listelerle çalıştık. Şimdi elemanları karışık veri tipleri olan hatta bir elemanı liste bile olabilen bir liste oluşturalım. İlgili videoyu izlemek için <a href="https://www.youtube.com/watch?v=yUcQvadgCrc">tıklayınız</a>. Videonun sonunda <b>mixed_list</b> isimli karışık listenin sonuna eklediğimiz listenin üçüncü elemanı olan 67.3'e <b><i>mixed_list[-1][2]</i></b> şeklinde eriştik.</p>

<b>mixed_list.py</b>

```
mixed_list = ["Muhammed", 19, 85.4, True]
mixed_list.append(["Eray", 20, 67.3, False])
print(f"mixed_list = {mixed_list}")
print(f"mixed_list[0] = {mixed_list[0]}")
print(f"type({mixed_list[0]}) = {type(mixed_list[0])}")
print(f"mixed_list[1] = {mixed_list[1]}")
print(f"type({mixed_list[1]}) = {type(mixed_list[1])}")
print(f"mixed_list[2] = {mixed_list[2]}")
print(f"type({mixed_list[2]}) = {type(mixed_list[2])}")
print(f"mixed_list[3] = {mixed_list[3]}")
print(f"type({mixed_list[3]}) = {type(mixed_list[3])}")
print(f"mixed_list[4] = {mixed_list[4]}")
print(f"type({mixed_list[4]}) = {type(mixed_list[4])}")
# listenin son elemanı olan listede 67.3'e erişmek istiyoruz
print(f"mixed_list[-1][2] = {mixed_list[-1][2]}")
```

<h4>LİSTENIN DEĞİŞİK YERLERİNE ELEMAN EKLEMEK</h4>
<p align="justify">Daha önceden <b><i>append()</i></b> metoduyla bir listeye sonundan eleman eklemiştik. Şimdi ise listenin istediğimiz bir konumuna eleman eklemek istiyoruz. Bunun için <b><i>insert()</i></b> isimli <b>liste metodunu</b> kullanacağız. Aşağıdaki örnekte listenin değişik konumlarına yeni isimler eklerken bir de mesela futbol maçında oyuncu değişikliği gibi bir öğrenci değişikliği yapıyoruz.Videoyu izlemek için <a href="https://www.youtube.com/watch?v=6Z9pkumcgVU">tıklayınız</a>.</p>

<b>adding_elements_to_list.py</b>

```
names = ["Arhan", "Mustafa", "Abdullah", "Jesuno", 
         "Bonaventura", "Abdulrahim", "Ziya"]
print(f"names = {names}")
print(f"İsimler listesinde {len(names)} eleman vardır.")
# listenin sonuna Rukiye'yi ekleyelim
names.append("Rukiye")
print(f"names = {names}")
# listenin başına Willy'i ekleyelim
names.insert(0, "Willy")
print(f"names = {names}")
# listenin sondan 3. sırasına Manuel'i ekleyelim
names.insert(-3, "Manuel")
print(f"names = {names}")
# listenin sonuna Taha'yı append() kullanmadan ekleyelim
names.insert(len(names), "Taha")
print(f"names = {names}")
# Abdullah'ı listeden çıkarıp Umut'u koyalım
names[3] = "Umut"
print(f"names = {names}")
```

<h4>LİSTENİN İSTEDİĞİMİZ BİR YERİNDEN ELEMAN ÇIKARMAK/SİLMEK</h4>

<p align="justify">Şu ana kadar listenin değişik konumlarına değişik veri tiplerinde elemanlar ekledik. Şimdi ise değişik liste metotlarıyla arzu edilen konumlardan elemanları çıkarmaya bakalım. Bu iş için kitabımızda da geçen <b><i>del()</i></b>, <b><i>pop()</i></b>, <b><i>remove()</i></b> gibi farklı metotlar kullanacağız. Yukarıda listeye eleman eklediğimiz kodun sonunda yaptığımız gibi burada da kodun en sonunda bir oyuncu değişikliği nevinden bir şey yapalım ama bu sefer index'i sayarak değil <b><i>index()</i></b> metoduyla otomatik elde ederek yapalım. Videoyu izlemek için <a href="https://www.youtube.com/watch?v=wPXNvc-Ro10">tıklayınız</a>.</p>

<b>removing_elements_from_list.py</b>

```
names = ['Willy', 'Arhan', 'Mustafa', 'Abdullah', 'Jesuno', 'Bonaventura', 
         'Manuel', 'Abdulrahim', 'Ziya', 'Rukiye', 'Taha']
print(f"names = {names}")
print(f"İsimler listesinde {len(names)} eleman vardır.")
# Arhan'ı listeden silmek istiyorum
names.remove(names[1])
print(f"names = {names}")
# listenin 3. elemanını silmek istiyorum
names.remove(names[2])
print(f"names = {names}")
# listenin son elemanını silmek istiyorum
names.remove(names[-1])
print(f"names = {names}")
# Abdulrahim'i de listeden ama bu sefer del komutuyla silelim
del names[-3]
print(f"names = {names}")
# Bonaventura'nın yerine Hande'yi koyalım
names[names.index("Bonaventura")] = "Hande"
print(f"names = {names}")
# pop() ile Jesuno'yu atalım
names.pop(2)
print(f"names = {names}")
```

<h4>LİSTEDEN ÇIKARDIĞIMIZ ELEMANLARLA YENİ BİR LİSTE OLUŞTURMAK</h4>

<p align="justify">Elimizdeki bir isim listesinin elemanlarını bir döngü ile dolaşarak harf sayısı altı veya daha fazla olan isimleri listeden çıkaralım. Yalnız çıkardığımız bu isimleri <b><i>remove()</i></b> metodu gibi <b>void</b> fonksiyonlarla (yâni geri bir değişken döndürmeyen fonksiyon) değil de <b><i>pop()</i></b> fonksiyonuyla yâni bize çıkardığımız ismi geri döndüren metotla yapalım. Döngüde çıkardığımız isimleri çıkarır çıkarmaz yeni bir listeye <b><i>append()</i></b> metoduyla ekliyor olacağız. <b>Not:</b> Kodu ilk önce <b>for</b> döngüsüyle yazmaya çalıştık ama karşılaştığımız <b>index</b> probleminden sonra <b>while</b> döngüsüne geçip <b>index</b> değerini kendimiz kontrol ederek problemin üstesinden geldik. İlgili videoyu izlemek için <a href="https://youtu.be/a7l9s5jUvRY?si=h9IZaOI5cfuEiQ4N">tıklayınız</a>.</p>

<b>making_new_list_from_list.py</b>

```
names = ['Willy', 'Arhan', 'Mustafa', 'Abdullah', 'Jesuno', 'Bonaventura', 
         'Manuel', 'Abdulrahim', 'Ziya', 'Rukiye', 'Taha', "İbrahim"]
print(f"Listenin ilk hâli = {names}")
print(f"İsimler listesinde {len(names)} eleman vardır.")
# isim listesinde harf sayısı 6 ve daha fazla olan isimleri 
# listeden atmak istiyorum ama attiğim isimleri yeni bir listede
# tutmak istiyorum ve bunu pop() metodu ile yapmak istiyorum
exported_names, k = [], 0
while k < len(names):
    if len(names[k]) >= 6:
        exported_names.append(names.pop(k))
    else:
        k += 1
print(f"Listenin son hâli = {names}")
print(f"İsimler listesinin son hâlinde {len(names)} eleman vardır.")
print(f"Çıkarılan isimler = {exported_names}")
print(f"Çıkarılanlar listesinde {len(exported_names)} eleman vardır.")
```