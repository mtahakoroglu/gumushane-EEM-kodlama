<h3>LİSTELERE GİRİŞ (INTRODUCING LISTS)</h3>

<h4>YEREL KLASÖRÜ GÜNCELLEME</h4>
<p align="justify">4. ve 5. haftada yaptığımız işleri bilgisayarınızda kendiniz yaparak dersin hocası ile aynı yere gelebilirsiniz. Ya da PowerShell ile "gumushane-EEM-bilgisayar-programlama" klasörünüzün bulunduğu dizine giderek</p>

```
git pull
```

<p align="justify">komutuyla "gumushane-EEM-bilgisayar-programlama" yerel klasörünüzü güncelleyebilirsiniz. İlgili videoyu <a href="https://youtu.be/q27HubmtPhc">izleyin</a>.</p>


<h4>BASİT BİR LİSTE ve INDEX ile LİSTENİN ELEMANLARINA ERİŞİM</h4>
<p align="justify">İlk önce basit bir liste oluşturalım. Bu liste kişi isimlerinden oluşsun ve ismi <b>names</b> olsun. Dolayısıyla bu listenin elemanlarının veri tipi (data type) string olacaktır. Aşağıdaki kod ile igili videoyu izlemek için <a href="https://youtu.be/BDl163lYLQ0" target="_blank">tıklayınız</a>. Listenin elemanlarına erişmek için <b>index</b> (Türkçesi <b>fihrist</b>) kullanılır.</p>

<p align="justify">ÖNEMLİ NOT: Bazı arkadaşlarımız normal parantez () ile kare parantezi [] ve dalgalı parantezi {} karıştırıyor. Liste oluştururken İngilizce'de <b>square brackets</b> denilen kare parantez kullanılıyor. Ekrana değişkenleri bastırmak için <b>formatted string</b> diye bilinen f-string kullanmıştık. Bu f-string'lerin içine değişkenleri İngilizce'de <b>curly brace</b> diye bilinen dalgalı parantez kullanarak yerleştirmiştik. Eğer normal parantez kullanılan yerde kare parantez veya dalgalı parantez kullanırsanız veya benzeri bir yanlış yaparsanız o zaman Python kodunuz hata verir. Bu hata için <a href="https://youtu.be/svwxJ6BKG1o">videoyu izleyiniz</a>.</p>

<b>simple_list.py</b>

```
names = ["Önder", "Furkan", "Sefa", "Safa", "Patrick", "Mahmoud", "Cindy"]
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
<p> Bu kısımda birden fazla basit liste tanımlıyoruz. Bu listelerin index'leri aynı olan elemanlarını uygun bir f-string ile mânâlı bir cümle oluşturacak şekilde ekrana yazdırmak için bir <b>for</b> döngüsü kullanıyoruz. Döngüleri henüz öğrenmediğimizden dolayı <b>GitHub Co-Pilot</b>'dan yardım aldık. İlgili video için <a href="https://www.youtube.com/watch?v=KnJXExjCgqE" target="_blank">tıklayınız</a>. Kodun üzerindeki yorumlardan da kodu anlayabilirsiniz.</p>

<b>multiple_list.py</b>

```
names = ["Önder", "Furkan", "Sefa", "Safa", "Patrick", "Mahmoud", "Cindy"]
ages = [20, 21, 21, 20, 23, 25, 24]
weight = [73.6, 75.2, 64.1, 67.9, 71.1, 68.1, 50.3]
attendance = [True, True, True, True, False, True, True]
# for döngüsü ile listedeki öğrencilerin isimlerini, yaşlarını ve kilolarını ekrana yazdıralım
for i in range(len(names)):
    if attendance[i]: # eğer öğrenci mevcut ise bilgileri yazdır
        print(f"{names[i]} {ages[i]} yaşında olup {weight[i]} kg ağırlığındadır.")
    else: # eğer öğrenci yok ise o zaman bilgileri yazdırma
        print(f"{names[i]} bugün sınıfta yoktur.")
```

<h4>BİR LİSTENİN ALT LİSTELERİNE SLICING ile (INDEX'ler KULLANARAK) ERİŞİM</h4>

<p align="justify">Bu kodda <b>names</b> isimli ana listeden <b>INDEX</b> değerlerini kullanarak değişik alt listeleri ve bazı durumlarda bu listelerin kombinasyonlarını kesiyoruz (<b>SLICING</b>). İlgili videoyu izlemek için <a href="https://youtu.be/hDPR_cEmaoM" target="_blank">tıklayınız</a>.</p>

<b>list_slicing.py</b>

```
names = ["Önder", "Furkan", "Sefa", "Safa", "Patrick", "Mahmoud", "Cindy"]
print(f"names = {names}") # isimler listesi
print(f"names[0:3] = {names[0:3]}") # ['Önder', 'Furkan', 'Sefa']
print(f"names[4:6] = {names[4:6]}") # ['Patrick', 'Mahmoud']
print(f"names[-2:] = {names[-2:]}") # ['Mahmoud', 'Cindy']
# Safa ile Patrick isimlerini yazdırmak istemiyoruz. Diğerlerini yazıralım.
print(f"names[:3] + names[5:] = {names[:3] + names[5:]}") # ['Önder', 'Furkan', 'Sefa', 'Mahmoud', 'Cindy']
# Sefa ile Patrick isimlerini yazdırmak istemiyoruz. Diğerlerini yazdıralım.
print(f"names[:2] + [names[3]] + names[-2:] = {names[:2] + [names[3]] + names[-2:]}") # ['Önder', 'Furkan', 'Safa', 'Mahmoud', 'Cindy']
```

<img src="./resim/list-slicing.jpg" alt="ana listeyi slicing kullanarak alt listelere ayırma" width=450 height=auto>