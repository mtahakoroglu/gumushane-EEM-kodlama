<h3>GİRİŞ</h3>
<p align="justify">Bu bölümde bilgisayarımıza Python resmi web sitesi olan <a href="https://python.org" target="_blank">https://python.org</a> adresinden Python yüklemeyi göreceğiz. Ayrıca PowerShell (PS) kullanımı ve Visual Studio Code (VS Code) yüklemeye de göz atacağız. Yüklemeler tamamlandıktan sonra <b>hello_world.py</b> isimli Python kodumuzu standart bir editörde yazıp PS'de koşturacağız. Ardından ders boyunca kullanacağımız Integrated Development Environment (IDE) olan VS Code'da kodumuzu koşturacağız.</p>

<b>hello_world.py</b>

```
print("Hello Python world!")
```

<h3>DEĞİŞKENLER ve BASİT VERİ TİPLERİ</h3>
<p align="justify">Bu bölümde değişkenlere (variables) ve basit veri tiplerine (data types) bakarken aynı zamanda <b>print()</b> komutuyla ekrana değişkenleri içeren ifadeler yazmayı <b>formatted string</b> ile yapacağız. Verileri kendimiz kodda tanımlamak yerine kullanıcıdan <b>input()</b> komutu ile alacağız. Bu komutun döndürdüğü bütün değişkenlerin tipinin <b>string</b> olduğunu görünce tam sayı (integer) ve ondalıklı sayı (floating point number veya decimal number) olarak girilen değerleri nasıl doğru biçimde yorumlayabileceğimizi göreceğiz. Son olarak da yine basit bir veri tipi olan Boolean değişkenlere bakıp ilk <b>if-else</b> koşullu ifademizi yazarak ekrana duruma göre bir yazı yazdıracağız. <b>Eğer-ise</b> şartlı ifadelerinde kullanılan Boolean değişkenler aynı zamanda gelecek haftalarda öğreneceğimiz döngülerde de kullanılacağından Boolean değişkenleri kavramak bizim için çok önemli.</p>

<b>hello_world_variables.py</b>

```
message = "Hello Python world!"
print(message)
```

<p>Burada ekrana direkt bir <b>string</b> literal yazdırmak yerine yazdırmak istediğimiz mesajı ilk önce <b>message</b> isminde bir değişkene atadık. Sonrasında bu değişkeni ekrana yazdırdık. Burada <b>message</b> isimli değişkenin veri tipinin <b>string</b> olduğunu aşağıdaki komutla görebiliriz.</p>

```
message = "Hello Python world!"
type(message)
```

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