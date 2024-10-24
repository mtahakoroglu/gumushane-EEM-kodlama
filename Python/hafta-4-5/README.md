<h3>LİSTELERE GİRİŞ (INTRODUCING LISTS)</h3>

<h4>YEREL KLASÖRÜ GÜNCELLEME</h4>
<p align="justify">4. ve 5. haftada yaptığımız işleri bilgisayarınızda kendiniz yaparak derin hocası ile aynı yere gelebilirsiniz. Ya da PowerShell ile "gumushane-EEM-bilgisayar-programlama" klasörünüzün bulunduğu dizine giderek</p>

```
git pull
```

<p align="justify">komutuyla "gumushane-EEM-bilgisayar-programlama" yerel klasörünüzü güncelleyebilirsiniz. İlgili videoyu <a href="https://youtu.be/q27HubmtPhc">izleyin</a>.</p>


<h4>BASİT BİR LİSTE ve LİSTENİN ELEMANLARINA ERİŞİM</h4>
<p align="justify">İlk önce basit bir liste oluşturalım. Bu liste kişi isimlerinden oluşsun ve ismi <b>names</b> olsun. Dolayısıyla bu listenin elemanlarının veri tipi (data type) string olacaktır. Aşağıdaki kodun yazıldığı ve koşturulduğu videoyu izlemek için <a href="https://youtu.be/BDl163lYLQ0" target="_blank">tıklayınız</a>.</p>

<p align="justify">ÖNEMLİ NOT: Bazı arkadaşlarımız normal parantez () ile kare parantezi [] karıştırıyor. Liste oluştururken İngilizce'de <b>square brackets</b> denilen kare parantez kullanılıyor. Eğer normal parantez kullanılan yerde kare parantez veya tam tersini yaparsanız o zaman Python kodunuz hata verir.</p>

<b>simple_list.py</b>

```
names = ["Önder", "Furkan", "Sefa", "Safa", "Patrick", "Mahmoud", "Cindy"]
print(f"names = {names}")
print(f"type(names) = {type(names)}")
print(f"type(names[0]) = {type(names[0])}")
print(f"Sınıfta {len(names)} öğrenci var.")
# listedeki isimleri tek tek ekrana yazdıralım
for name in names:
    print(name)
```

