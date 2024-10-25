<h3>LİSTELERE GİRİŞ (INTRODUCING LISTS)</h3>

<h4>YEREL KLASÖRÜ GÜNCELLEME</h4>
<p align="justify">4. ve 5. haftada yaptığımız işleri bilgisayarınızda kendiniz yaparak dersin hocası ile aynı yere gelebilirsiniz. Ya da PowerShell ile "gumushane-EEM-bilgisayar-programlama" klasörünüzün bulunduğu dizine giderek</p>

```
git pull
```

<p align="justify">komutuyla "gumushane-EEM-bilgisayar-programlama" yerel klasörünüzü güncelleyebilirsiniz. İlgili videoyu <a href="https://youtu.be/q27HubmtPhc">izleyin</a>.</p>


<h4>BASİT BİR LİSTE ve LİSTENİN ELEMANLARINA ERİŞİM</h4>
<p align="justify">İlk önce basit bir liste oluşturalım. Bu liste kişi isimlerinden oluşsun ve ismi <b>names</b> olsun. Dolayısıyla bu listenin elemanlarının veri tipi (data type) string olacaktır. Aşağıdaki kodun yazıldığı ve koşturulduğu videoyu izlemek için <a href="https://youtu.be/BDl163lYLQ0" target="_blank">tıklayınız</a>.</p>

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

<h4>BİRDEN ÇOK LİSTE ve EKRANA FOR DÖNGÜSÜ ile LİSTE BİLGİLERİNİN YAZDIRILMASI</h4>

<p align="justify">Yukarıda ismi <b>names</b> olan elemanlarının veri tipi (data type) <b>string</b> olan bir liste tanımlamıştık. Burada o listeye eşlik eden üç ayrı liste daha tanımlayıp bu listelerin elemanlarını f-string kullanarak ekrana yazdıralım. İlgili videoyu izlemek için <a href="https://youtu.be/KnJXExjCgqE">tıklayınız</a>. Burada listelerin elemanlarını teker teker ekrana yazdırmak için bir <b>for</b> döngüsü kullanıyoruz. Bu konuyu daha işlemediğimizden ve tam olarak <b>syntax</b>'ini bilmediğimizden GitHub Co-Pilot'dan yardım aldık. Videoda görebilirsiniz.</p>

<b>multiple_list.py</b>

```
names = ["Önder", "Furkan", "Sefa", "Safa", "Patrick", "Mahmoud", "Cindy"]
ages = [20, 21, 21, 20, 23, 25, 24]
weight = [73.6, 75.2, 64.1, 67.9, 71.1, 68.1, 50.3]
attendance = [True, True, True, True, False, True, True]
# for döngüsü ile listedeki öğrencilerin isimlerini, yaşlarını, kilolarını ve devamsızlık durumlarını ekrana yazdıralım
for i in range(len(names)):
    if attendance[i]:
        print(f"{names[i]} {ages[i]} yaşında olup {weight[i]} kg ağırlığındadır.")
    else:
        print(f"{names[i]} bugün sınıfta yoktur.")
```
