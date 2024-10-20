<h3>GİRİŞ</h3>
<p align="justify">Bu bölümde bilgisayarımıza Python resmi web sitesi olan <a href="https://python.org" target="_blank">https://python.org</a> adresinden Python yüklemeyi göreceğiz. Ayrıca PowerShell (PS) kullanımı ve Visual Studio Code (VS Code) yüklemeye de göz atacağız. Yüklemeler tamamlandıktan sonra <b>hello_world.py</b> isimli Python kodumuzu standart bir editörde yazıp PS'de koşturacağız. Ardından ders boyunca kullanacağımız Integrated Development Environment (IDE) olan VS Code'da kodumuzu koşturacağız.</p>

<h3>DERSTE GITHUB KULLANIMI</h3>
<p align="justify">Bilgisayarınızda git yüklü olmalı. İlk olarak PS açıp, bilgisayarınızda çalışacağınız dizine gidip orada</p>

```
git clone https://github.com/mtahakoroglu/gumushane-EEM-bilgisayar-programlama.git
```

<p align="justify">komutunu koşturursanız o zaman bulunduğunuz dizine ders sayfamızdaki bilgiler ve kodlar indirilecektir (<a href="https://youtu.be/HvAsIwK6Ka0">GitHub clone videosunu izleyin</a>). İlerleyen haftalarda her zaman <b>clone</b> komutuyla sıfırdan indirme yapmayıp, dersin hocasının kod deposuna koyduğu yeni materyalleri <b>pull</b> komutuyla indirerek bilgisayarınızda derse ait <b>gumushane-EEM-bilgisayar-programlama</b> klasörünü güncelleyebiliriniz.</p>

<h3>İLK PYTHON KODUMUZ</h3>

<p align="justify">Ekrana "Merhaba Dünya!" yazdıralım.</p>

<b>hello_world.py</b>

```
print("Merhaba Dünya!")
```

<h3>DEĞİŞKENLER ve BASİT VERİ TİPLERİ</h3>

<p align="justify">Ekrana yine "Merhaba Dünya!" yazdıralım. Fakat bu sefer "Merhaba Dünya!" yazısı kodun içinde bir değişkene atanmış olsun ve bu değişkeni <b>print()</b> fonksşyonuna yollayalım.</p>

<b>hello_world_variables.py</b>

```
message = "Merhaba Dünya!"
print(message)
```

<p>Burada ekrana direkt bir <b>string</b> literal yazdırmak yerine yazdırmak istediğimiz mesajı ilk önce <b>message</b> isminde bir değişkene atadık. Sonrasında bu değişkeni ekrana yazdırdık. Burada <b>message</b> isimli değişkenin veri tipinin <b>string</b> olduğunu aşağıdaki komutla görebiliriz.</p>

```
message = "Merhaba Dünya!"
type(message)
```

<p align="justify">Bu bölümde değişkenlere (variables) ve basit veri tiplerine (data types) bakarken aynı zamanda <b>print()</b> komutuyla ekrana değişkenleri içeren ifadeler yazmayı <b>formatted string</b> ile yapacağız. Verileri kendimiz kodda tanımlamak yerine kullanıcıdan <b>input()</b> komutu ile alacağız. Bu komutun döndürdüğü bütün değişkenlerin tipinin <b>string</b> olduğunu görünce tam sayı (integer) ve ondalıklı sayı (floating point number veya decimal number) olarak girilen değerleri nasıl doğru biçimde yorumlayabileceğimizi göreceğiz. Son olarak da yine basit bir veri tipi olan Boolean değişkenlere bakıp ilk <b>if-else</b> koşullu ifademizi yazarak ekrana duruma göre değişiklik gösteren bir yazı yazdıracağız. <b>Eğer-ise</b> şartlı ifadelerinde kullanılan Boolean değişkenler aynı zamanda gelecek haftalarda öğreneceğimiz döngülerde de kullanılacağından Boolean değişkenleri kavramak bizim için çok önemli. Bu sayfadaki kodların koşturulmasını izlemek için <a href="https://youtu.be/HvAsIwK6Ka0?si=WcsRYufEqoCsjsJV&t=277">tıklayınız</a>.</p>

<b>user_input_data_types_fstring.py</b>

```
name = input("Kişinin ismi ne? ")
age = int(input(f"{name} isimli kişinin yaşı kaç? "))
weight = float(input(f"{name} isimli kişi kaç kg? "))
x, year, chernobylYear = 5, 2024, 1986
birthYear = year - age
print(f"{name} {birthYear} senesinde doğmuştur.")
print(f"{name} eğer {x}kg daha alırsa {weight+x}kg olacaktır.")
if chernobylYear > birthYear:
    print(f"{name} Chernobyl faciasından önce doğmuştur.")
elif chernobylYear == birthYear:
    print(f"{name} Chernobyl faciasıyla aynı senede doğmuştur.")
else:
    print(f"{name} Chernobyl faciasından sonra doğmuştur.")
```

<p>Yukarıdaki kodun sonuna aşağıda <b>type()</b> komutu içeren satırları ekleyerek dört basit veri tipini ekranda görüntüleyebiliriz.</p>

```
print(f"type(name) = {type(name)}")
print(f"type(age) = {type(age)}")
print(f"type(weight) = {type(weight)}")
print(f"type(chernobylYear > birthYear) = {type(chernobylYear > birthYear)}")
```