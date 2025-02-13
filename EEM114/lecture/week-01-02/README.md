<h3>GİRİŞ</h3>
<p align="justify">Bilgisayarımıza Python resmi web sitesi olan <a href="https://python.org" target="_blank">https://python.org</a> adresinden Python yükleyebiliriz. Ayrıca PowerShell (PS) ve Visual Studio Code (VS Code) kullanmaya aşina olmalıyız. Python ve VS Code yüklemeleri tamamlandıktan sonra <b>hello_world.py</b> isimli ilk Python kodumuzu standart bir editörde yazıp ilk önce PS'de, sonrasında da ders boyunca kullanacağımız Integrated Development Environment (IDE) olan VS Code'da koşturacağız. Dersimizi yapacağımız Ümit Uzman Lab.'daki bilgisayarlarda Python ve VS Code yüklü hâlde. Kendi bilgisayarlarında kodlama yapacak olan arkadaşlarımız kurulumları kendileri yapsınlar. Problemlerle karşılaşanlar bana sorabilirler. Ben genelde Şehit Öğretmen Necmettin Yılmaz Lab.'da bulunuyorum.</p>

<h4>DERSTE GITHUB KULLANIMI</h4>

<p align="justify">Bilgisayarınızda <b>git</b> yüklü olursa çok iyi olur. Bilgisayarda PS'i açıp, bilgisayarınızda çalışacağınız dizine <b>cd</b> komutlarıyla gidip</p>

```
git clone https://github.com/mtahakoroglu/gumushane-EEM-kodlama.git
```

<p align="justify">komutunu koşturursanız, o zaman bulunduğunuz dizine ders sayfamızdaki bilgiler ve kodlar indirilecektir. İlerleyen haftalarda her zaman <b>clone</b> komutuyla sıfırdan indirme yapmayıp, dersin hocasının kod deposuna koyduğu yeni materyalleri <b>pull</b> komutuyla indirerek lokal <b>gumushane-EEM-kodlama</b> klasörünüzü güncelleyebiliriniz. Tabi bu yazanlar kendi kodlarını yazmayan veya bazı derslere gelmeyip de en son hocanın kaldığı yerden devam etmek isteyenler için geçerli. Yâni, bilgisayarlarında kendi kodlarını yazanların burada anlatılan <b>git</b> sistemiyle derse ait repo'yu indirme ihtiyaçları olmayacaktır.</p>

<h4>İLK PYTHON KODUMUZ</h4>

<p align="justify">Ekrana "Merhaba Dünya!" yazdıralım.</p>

<b>hello_world.py</b>

```
print("Merhaba Dünya!")
```

<h3>DEĞİŞKENLER ve BASİT VERİ TİPLERİ</h3>

<p align="justify">Ekrana yine "Merhaba Dünya!" yazdıralım. Fakat bu sefer "Merhaba Dünya!" yazısı kodun içinde bir değişkene atanmış olsun ve bu değişkeni <b>print()</b> fonksiyonuna yollayalım.</p>

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

<p align="justify">Yukarıdaki kodu koşturursak, terminale</p>

<b><class 'str'></b>

<p align="justify">yazdırdığını göreceksiniz. Yâni message değişkeni veri tipi olarak <b>string</b> demek. Aşağıda öbür basit veri tipleri olan <b>int</b>, <b>float</b> ve <b>bool</b> tipinde değişkenlere de bakacağız.</p>

<h4>input() fonksiyonu ve f-string kullanımı</h4>

<p align="justify">Bu bölümde değişkenlere (variables) ve basit veri tiplerine (data types) bakarken aynı zamanda <b>print()</b> komutuyla ekrana değişkenleri içeren ifadeler yazmayı <b>f-string</b> olarak bilinen <b>formatted string</b> ile yâni <b>formatlanmış string</b> ile yapacağız. Verileri kendimiz kodda oluşturmak yerine konsolda kullanıcıdan <b>input()</b> komutu ile alacağız. Aşağıdaki kodu koşturalım.</p>

<b>input_fstring.py</b>

```
name = input("İsminiz nedir? ")
print(f"Merhaba {name}!")
age = input("Yaşın kaç? ")
print(f"10 sene sonra {age+10} yaşında olacaksın.")
```

<p align="justify">Kodu koşturunca verilen hatadan <b>input()</b> fonksiyonunun döndürdüğü değişkenin veri tipinin <b>string</b> olduğunu, yâni bilgisayarın bunu bir sayı olarak görmediğini anlıyoruz. Burada <b>int()</b> fonksiyonunu kullanarak tam sayı (integer) olarak girilen değeri doğru biçimde dönüştürerek hesabı hatasız yapalım ve ekrana 10 sene sonraki yaşımızı yazdıralım.</p>

<b>input_fstring_int.py</b>

```
name = input("İsminiz nedir? ")
print(f"Merhaba {name}!")
age = int(input("Yaşın kaç? "))
print(f"10 sene sonra {age+10} yaşında olacaksın.")
```

<p align="justify">Son olarak da yine basit bir veri tipi olan Boolean değişkenlere bakıp ilk <b>if-else</b> koşullu ifademizi yazarak ekranda duruma göre değişiklik gösteren bir yazı yazalım. <b>Eğer-ise</b> şartlı ifadelerinde kullanılan Boolean değişkenler aynı zamanda gelecek haftalarda öğreneceğimiz döngülerde de kullanılacağından Boolean değişkenleri kavramak bizim için çok önemli.</p>

<b>input_data_types_fstring.py</b>

```
name = input("İsminiz nedir? ")
age = int(input(f"Merhaba {name}! Kaç yaşındasın? "))
print(f"10 sene sonra {age+10} yaşında olacaksın.")
weight = float(input("Kaç kilosun {name}? "))
weightInt = round(weight)
print(f"Yuvarlak hesap {weightInt}kg diyebiliriz.")
height = int(input("Peki boyun (cm olarak) kaç? "))
# Burada kilo-boy oranına kabaca bakalım ve duruma göre ekrana mesaj yazalım
if height-100 > weightInt:
    print("Biraz kilo alsan iyi olur!")
elif height-100 == weightInt:
    print("Boyuna göre kilon iyi!")
else:
    print("Biraz kilo versen iyi olur!")
```

<p align="justify">Yukarıdaki kodun sonuna aşağıda <b>type()</b> fonksiyonunu içeren satırları ekleyerek dört basit veri tipini ekranda görüntüleyebiliriz. Gerçek hayatta veri tipleri karşımıza çıkacağından <b>type()</b> fonksiyonu mutlaka anlaşılmalı.</p>

```
print(f"type(name) = {type(name)}")
print(f"type(age) = {type(age)}")
print(f"type(weight) = {type(weight)}")
print(f"type(height-100 > weightInt) = {type(height-100 > weightInt)}")
```

<p align="justify">Ayrıca kodun sonunda girilen bütün değişkenleri kullanarak bir cümle oluşturup bu cümleyi fstring'lerle ekrana basma alıştırmasını da yapınız.</p>

```
print(f"{name}, {age} yaşında {weight}kg {height}cm boyunda birisidir.")
```

<p align="justify"><b>Alıştırma:</b> Gerekli değişikleri yaparak (GitHub Copilot gibi asistanlardan faydalanabilirsiniz) ekrana boyu metre cinsinden yazdırınız.</p>