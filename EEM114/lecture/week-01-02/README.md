<h3>GİRİŞ</h3>
<p align="justify">Bilgisayarımıza Python resmi web sitesi olan <a href="https://python.org" target="_blank">https://python.org</a> adresinden Python yükleyebiliriz. Ayrıca PowerShell (PS) kullanımı ve Visual Studio Code (VS Code) kullanmaya aşina olmalıyız. Python ve VS Code yüklemeleri tamamlandıktan sonra <b>hello_world.py</b> isimli Python kodumuzu standart bir editörde yazıp PS'de koşturacağız. Ardından ders boyunca kullanacağımız Integrated Development Environment (IDE) olan VS Code'da kodumuzu koşturacağız. Dersimizi yapacağımız Ümit Uzman Lab.'da Python ve VS Code yüklü oluyor. Kendi bilgisayarlarında kodlama yapacak olan arkadaşlarımızda kurulumları kendileri yapsınlar. Problemlerle karşılaşanlar bana sorabilirler.</p>

<h3>DERSTE GITHUB KULLANIMI</h3>

<p align="justify">Bilgisayarınızda git yüklü olmalı. İlk olarak PS açıp, bilgisayarınızda çalışacağınız dizine gidip orada</p>

```
git clone https://github.com/mtahakoroglu/gumushane-EEM-kodlama.git
```

<p align="justify">komutunu koşturursanız o zaman bulunduğunuz dizine ders sayfamızdaki bilgiler ve kodlar indirilecektir. İlerleyen haftalarda her zaman <b>clone</b> komutuyla sıfırdan indirme yapmayıp, dersin hocasının kod deposuna koyduğu yeni materyalleri <b>pull</b> komutuyla indirerek lokal <b>gumushane-EEM-kodlama</b> klasörünüzü güncelleyebiliriniz.</p>

<h3>İLK PYTHON KODUMUZ</h3>

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

<p align="justify">Bu bölümde değişkenlere (variables) ve basit veri tiplerine (data types) bakarken aynı zamanda <b>print()</b> komutuyla ekrana değişkenleri içeren ifadeler yazmayı <b>f-string</b> olarak bilinen <b>formatted string</b> ile yâni <b>formatlanmış string</b> ile yapacağız. Verileri kendimiz kodda oluşturmak yerine konsolda kullanıcıdan <b>input()</b> komutu ile alacağız. Bu komutun döndürdüğü bütün değişkenlerin tipinin <b>string</b> olduğunu görünce tam sayı (integer) ve ondalıklı sayı (floating point number veya decimal number) olarak girilen değerleri nasıl doğru biçimde dönüştürebileceğimizi göreceğiz. Son olarak da yine basit bir veri tipi olan Boolean değişkenlere bakıp ilk <b>if-else</b> koşullu ifademizi yazarak ekranda duruma göre değişiklik gösteren bir yazı yazdıracağız. <b>Eğer-ise</b> şartlı ifadelerinde kullanılan Boolean değişkenler aynı zamanda gelecek haftalarda öğreneceğimiz döngülerde de kullanılacağından Boolean değişkenleri kavramak bizim için çok önemli. Bu sayfadaki kodların koşturulmasını izlemek için <a href="https://youtu.be/ld0Vp_i5u8o">tıklayınız</a>.</p>

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

<p>Yukarıdaki kodun sonuna aşağıda <b>type()</b> komutu içeren satırları ekleyerek dört basit veri tipini ekranda görüntüleyebiliriz. Sınavlarda <b>type()</b> komutu karşımıza çıkacağından mutlaka anlaşılmalı.</p>

```
print(f"type(name) = {type(name)}")
print(f"type(age) = {type(age)}")
print(f"type(weight) = {type(weight)}")
print(f"type(chernobylYear > birthYear) = {type(chernobylYear > birthYear)}")
```