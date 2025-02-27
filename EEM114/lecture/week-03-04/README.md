<h3>LİSTELERE GİRİŞ (INTRODUCING LISTS)</h3>

<h4>BASİT BİR LİSTE ve INDEX ile LİSTENİN ELEMANLARINA ERİŞİM</h4>
<p align="justify">İlk önce basit bir liste oluşturalım. Bu liste kişi isimlerinden oluşsun ve ismi <b>names</b> olsun. Dolayısıyla bu listenin elemanlarının veri tipi (data type) string olacaktır. Aşağıdaki kod ile igili videoyu izlemek için <a href="https://www.youtube.com/watch?v=wd1OUB35HzM" target="_blank">tıklayınız</a>. Listenin elemanlarına erişmek için <b>index</b> (Türkçesi <b>fihrist</b>) kullanılır.</p>

<p align="justify">ÖNEMLİ NOT: Bazı arkadaşlarımız normal parantez () ile kare parantezi [] ve dalgalı parantezi {} karıştırıyor. Liste oluştururken İngilizce'de <b>square brackets</b> denilen kare parantez kullanılıyor. Ekrana değişkenleri bastırmak için <b>formatted string</b> diye bilinen f-string kullanmıştık. Bu f-string'lerin içine ilgili değişkenleri İngilizce'de <b>curly brace</b> diye bilinen dalgalı parantez (süslü parantez) kullanarak yerleştirmiştik. Eğer normal parantez kullanılan yerde kare parantez veya dalgalı parantez kullanırsanız veya benzeri bir yanlış yaparsanız o zaman Python kodunuz hata verir.</p>

<b>simple_list.py</b>

```
names = ["Arhan", "Mustafa", "Abdullah", "Jesuno", "Bonaventura", "Abdulrahim", "Ziya"]
print(f"names = {names}")
print(f"type(names) = {type(names)}")
print(f"names[0] = {names[0]}")
print(f"names[1] = {names[1]}")
print(f"names[2] = {names[2]}")
print(f"names[5] = {names[5]}")
print(f"names[6] = {names[6]}")
print(f"names[-1] = {names[-1]}")
print(f"names[-2] = {names[-2]}")
print(f"type(names[1]) = {type(names[1])}")
print(f"Sınıfta {len(names)} öğrenci var.")
# listedeki isimleri tek tek ekrana yazdıralım
for name in names:
    print(name)
```

<h4>ELEMANLARI DEĞİŞİK VERİ TİPLERİ OLAN LİSTELER</h4>

<p align="justify">Yukarıda ismi <b>names</b> olan elemanlarının veri tipi (data type) <b>string</b> olan bir liste tanımlamıştık. Burada o listeye eşlik eden üç ayrı liste daha tanımlayacağız.</p>

<h5>FOR DÖNGÜSÜ ile LİSTE ELEMANLARINI F-STRING KULLANARAK EKRANA YAZIRMAK</h5>

<p> Bu kısımda birden fazla basit liste tanımlıyoruz. Bu listelerin index'leri aynı olan elemanlarını uygun bir f-string ile mânâlı bir cümle oluşturacak şekilde ekrana yazdırmak için bir <b>for</b> döngüsü kullanıyoruz. Döngüleri henüz öğrenmediğimizden dolayı <b>GitHub Co-Pilot</b>'dan yardım aldık. İlgili video için <a href="https://www.youtube.com/watch?v=xI4zx4jV97E" target="_blank">tıklayınız</a>. Kodun üzerindeki yorumlardan da kodu anlayabilirsiniz.</p>

<b>multiple_list.py</b>

```
names = ["Arhan", "Mustafa", "Abdullah", "Jesuno", "Bonaventura", "Abdulrahim", "Ziya"]
ages = [21, 21, 20, 19, 22, 21, 19]
weight = [91.1, 64.2, 85.3, 79.6, 80.4, 65.7, 69.4]
attendance = [True, True, True, False, True, False, True]
# bir döngü ile listedeki elemanlardan mânâlı cümle oluşturalım ve ekrana basalım
for i in range(len(names)): # listeleri i indeksi ile dolaşıyoruz
    if attendance[i]:
        print(f"{names[i]}, {ages[i]} yaşında, {weight[i]}kg ağırlığında bir öğrencidir.")
    else:
        print(f"{names[i]} bugün derse gelmedi.")
```

<h4>BİR LİSTENİN ALT LİSTELERİNE SLICING ile (INDEX'ler KULLANARAK) ERİŞİM</h4>

<p align="justify">Bu kodda <b>names</b> isimli ana listeden <b>INDEX</b> değerlerini kullanarak değişik alt listeleri kesiyoruz (<b>SLICING</b>). İlgili videoyu izlemek için <a href="https://www.youtube.com/watch?v=2qBpemP8zuw" target="_blank">tıklayınız</a>.</p>

<b>list_slicing.py</b>

```
names = ["Arhan", "Mustafa", "Abdullah", "Jesuno", 
         "Bonaventura", "Abdulrahim", "Ziya", "Umut",
         "Eray", "İbo"]
print(f"names = {names}")
print(f"İlk üç öğrenci: names[0:3] = {names[0:3]}")
print(f"İlk üç öğrenci: names[:3] = {names[:3]}")
print(f"names[-5:-2] = {names[-5:-2]}")
print(f"Son üç öğrenci: names[-3:] = {names[-3:]}")
```

<h4>LİSTE METOTLARINA GİRİŞ</h4>

<p align="justify">Listelere ait <b>title()</b>, <b>upper()</b> ve <b>lower()</b> isimli metotlara bakalım. Kitapta <b>rstrip()</b>, <b>lstrip()</b> ve <b>strip()</b> mettoları da geçiyor. İlgili videoyu izlemek için <a href="https://youtu.be/z_o6j1uvPYU" target="_blank">tıklayınız</a>.</p>

<b>list_methods.py</b>

```
names = ["Arhan", "mustafa", "aBdULLah", "JESUNO", 
         "bonaventurA", "AbdulRahim", "ziYA", "Umut",
         "eray", "ibo"]
print(names)
# liste metotları kullarak isimleri değişik formlarda ekrana basalım
print("İlk harfler büyük diğerleri küçük")
for name in names:
    print(name.title(), end=" ")
print("\nİsimlerdeki harflerin tamamı büyük") # \n bir alt satıra geçer
for name in names:
    print(name.upper(), end=" ")
print("\nİsimlerdeki harflerin tamamı küçük")
for name in names:
    print(name.lower(), end=" ")
# kitapta rstrip(), lstrip(), strip() metotları da kullanılmış
name = "     Arhan"
print(f"\nname = {name}    name.lstrip() = {name.lstrip()}")
name = "Arhan     "
print(f"name = {name}    name.rstrip() = {name.rstrip()}")
name = "    Arhan    "
print(f"name = {name}    name.strip() = {name.strip()}")
```

<h4>DİNAMİK LİSTE OLUŞTURMA</h4>

<p align="justify">Listelere ait <b>append()</b> isimli metot ile kullanıcı tarafından girişi yapılan liste elemanlarını sıra sıra listeye kaydedelim ve en sonunda hem <b>len()</b> komutuyla hem de kendi sayıcımızla listenin uzunluğunu hesaplayarak liste ile ekrana basalım. İlgili videoyu izlemek için <a href="https://youtu.be/z_o6j1uvPYU" target="_blank">tıklayınız</a>.</p>

<b>user_input_dynamic_list.py</b>

```
names = []

k = 0 # listeye eklenen isimleri kendimiz sayalım
while True:
    s = int(input("İsim eklemek için 1'e, programı sonlandırmak için 2'a basınız: "))
    if s == 1:
        names.append(input("İsim giriniz: "))
        k += 1 # k = k+1
    elif s == 2:
        print("Program sonlandırıldı.")
        break
    else:
        print("Hatalı giriş yaptınız! Lütfen tekrar deneyiniz.")

print(f"names = {names}") # isimler listesi
print(f"names isimli listenin uzunluğu: {len(names)}") # isimler listesinin uzunluğu
print(f"names isimli listenin kendi sayımımıza göre uzunluğu: {k}") # isimler listesinin uzunluğu
```