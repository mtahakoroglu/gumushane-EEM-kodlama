<h3>IF İFADELERİ</h3>

<p align="justify">İçerisinde VE ve VEYA mantık kapılarını (AND and OR logic gates) tekrar ettiğimiz koşullu ifade örnek kodunun çıktısını görmek için <a href="https://www.youtube.com">tıklayınız</a>.</p>

```
flag1, flag2 = False, True
if flag1:
    print("Merhaba!")
elif flag1 and True:
    print("Hola!")
elif flag1 or not flag2:
    print("Hello!")
elif not flag2:
    print("Güle güle dostum.")
elif not flag1 and flag2:
    print("Adios amigo.")
else:
    print("Good bye dude.")
```

<h4>Python Listelerinde Döngü, Koşullu İfade ve String Metotları Egzersizleri</h4>

<p align="justify">Aşağıda ders kitabından aldığımız <b>cars.py</b> kodunu bulabilirsiniz. İlgili video için <a href="https://www.youtube.com/watch?v=jaXPlEWvgxQ">tıklayınız</a>.</p>

<p align="justify"><b>cars.py</b></p>

```
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

<p align="justify">Aşağıda ders kitabından aldığımız <b>cars.py</b> kodundan hareketle kendi ürettiğimiz <b>names.py</b> kodunu bulabilirsiniz. İlgili video için <a href="https://www.youtube.com/watch?v=IgQNqG20otU">tıklayınız</a>.</p>

<p align="justify"><b>names.py</b></p>

```
names = ['Rukiye', 'Handenur', 'Abdullah', 'İbrahim', 'Rana']
for name in names:
    if name[0].lower() == 'r':
        print(name.upper())
    else:
        print(name.lower())
```

<h4>Başka Bir Örnek (if-else if-else koşullu ifadeleri)</h4>

<p align="justify">Kitaptan koşullu ifadelerle ilgili bir başka örnek: <b>hayat.py</b> isimli kodun videosu için <a href="https://www.youtube.com/watch?v=SChaa65x1Lo&list=PLMoe16OQDeeCpsXqSpWs0LqOYUjlIu_jg&index=28">tıklayınız</a>.</p>

<p align="justify">(Hayatın Aşamaları): Bir insanın hayatta hangi aşamada olduğunu belirleyen bir if-elif-else zinciri yazınız. Kullanıcıya yaşını sorarak kullanıcının girdiği değeri <b>age</b> değişkenine atayın ve daha sonra:</p>

<ul>
<li>Kişi 2 yaşından küçük ise bu kişinin bebek olduğunu belirten bir mesajı ekrana yazdırınız.</li>
<li>Kişi en az 2 yaşında ama 4 yaşından küçük ise bu kişinin yürümeye yeni başlayan bir çocuk olduğunu belirten bir mesajı ekrana yazdırınız.</li>
<li>Kişi en az 4 yaşında ama 13 yaşından küçük ise bu kişinin çocuk olduğunu belirten bir mesajı ekrana yazdırınız.</li>
<li>Kişi en az 13 yaşında ama 20 yaşından küçük ise bu kişinin ergen olduğunu belirten bir mesaj ekrana yazdırınız.</li>
<li>Kişi en az 20 yaşında ama 65 yaşından küçük ise bu kişinin yetişkin olduğunu belirten bir mesajı ekrana yazdırınız.</li>
<li>Kişi 65 yaş ve üzeri ise bu kişinin yaşlı olduğunu belirten bir mesajı ekrana yazınız.</li>
</ul>

<p align="justify"><b>hayat.py</b></p>

```
age = int(input("Kaç yaşındasın? "))
if age < 2:
    print("Daha bebeksin.")
elif age < 4:
    print("Henüz yürümeye başladın.")
elif age < 13:
    print("Çocuksun.")
elif age < 20:
    print("Gençsin.")
elif age < 65:
    print("Yetişkinsin.")
else:
    print("Yaşlısın.")
```

<p align="justify">Another example about the conditional statements (from the course book): <b>stages_in_life.py</b> click on the <a href="https://www.youtube.com/watch?v=tOWbycYozGk&list=PLMoe16OQDeeCpsXqSpWs0LqOYUjlIu_jg&index=29">link</a> to watch the related video.</p>

<p align="justify">(Stages of Life): Write an if-elif-else chain that determines a person's stage of life. Get the user's age by asking him/her a related question in the console and assign the entered value to <b>age</b> variable and then:</p>

<ul>
<li>If the person is less than 2 years old, print a message that the person is a baby.</li>
<li>If the person is at least 2 years old but less than 4, print a message that the person is a toddler.</li>
<li>If the person is at least 4 years old but less than 13, print a message that the person is a kid.</li>
<li>If the person is at least 13 years old but less than 20, print a message that the person is a teenager.</li>
<li>If the person is at least 20 years old but less than 65, print a message that the person is an adult.</li>
<li>If the person is age 65 or older, print a message that the person is an elder.</li>
</ul>

<b>stages_in_life.py</b>

```
age = int(input("How old are you? "))
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")
```