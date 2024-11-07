<h3>LİSTELERLE ÇALIŞMAK (WORKING with LISTS)</h3>

<h4>KARIŞIK LİSTE</h4>
<p align="justify">Şu ana kadar (4. ve 5. haftalarda) elemanları string, integer, float veya bool veri tipi olan listelerle çalıştık. Şimdi elemanları karışık veri tipleri olan hatta bir elemanı liste bile olabilen bir liste oluşturalım. İlgili videoyu izlemek için <a href="https://www.youtube.com/watch?v=ZvD-vRrwTZA">tıklayınız</a>. Videoda yer almayan son kısımda <b>mixed_list</b> isimli karışık listenin sonuna eklediğimiz listenin ilk elemanına <b><i>mixed_list[-1][0]</i></b> eriştik.</p>

<b>mixed_list.py</b>

```
mixed_list = ["Sefa", 21, 64.1, True]
print(f"mixed_list = {mixed_list}")
mixed_list.append(["Patrick", 22, 67.3, False])
print(f"mixed_list = {mixed_list}")
# listenin son elemanı olan listenin ilk elemanına erişelim
print(f"mixed_list[-1][0] = {mixed_list[-1][0]}")
```

<h4>LİSTENİN İSTEDİĞİMİZ BİR YERİNE ELEMAN EKLEMEK</h4>

<p align="justify">Daha önceden <b><i>append()</i></b> metoduyla bir listeye sonundan eleman eklemiştik. Şimdi ise listenin istediğimiz bir konumuna eleman eklemek istiyoruz. Bunun için <b><i>insert()</i></b> isimli liste metodunu kullanacağız. Aşağıdaki örnekte listenin değişik konumlarına yeni isimler eklerken bir de oyuncu değişikliği benzeri öğrenci değişikliği yapıyoruz.</p>

<b>adding_elements_to_list.py</b>

```
names = ["Safa", "Mahmoud", "Abdullah", "Nour"] # ilk oluşturulan liste
names.insert(1, "Tabarak") # 2. sıraya Tabarak'ı ekleyelim
names.insert(0, "Çınay") # ilk sıraya Çınay'ı ekleyelim
# Mahmoud'un yerine listeye Abdurrahman'ı listeye almaya karar verdik
names[3] = "Abdurrahman"
# listenin sonuna Önder'i ekleyelim
names.append("Önder")
```

<h4>LİSTENİN İSTEDİĞİMİZ BİR YERİNDENE ELEMAN ÇIKARMAK/SİLMEK</h4>

<p align="justify">Şu ana kadar listenin değişik konumlarına değişik veri tiplerinde elemanlar ekledik. Şimdi ise değişik liste metotlarıyla arzu edilen konumlardan elemanları çıkarmaya bakalım. Bu iş için <b><i>del</i></b>, <b><i>pop()</i></b>, <b><i>remove()</i></b> gibi farklı metotlar kullanacağız.</p>

<b>removing_elements_from_list.py</b>

```
names = ['Çınay', 'Safa', 'Tabarak', 'Abdurrahman', 'Abdullah', 'Nour', 'Önder']
del names[2] # 3. eleman olan Tabarak'i listeden çıkaralım
names.remove('Nour') # Nour'u da listeden çıkaralım
last_person = names.pop() # listenin son elemanını çıkaralım
print(f"Listenin sonunda {last_person} vardı. Onu da çıkardık.")
# şimdi pop() metoduyla listenin istediğimiz bir konumundan bir eleman çıkaralım
second_person = names.pop(1) # 2. eleman olan Safa'yı listeden çıkaralım
print(f"İkinci sıradaki kişi olan {second_person} listeden çıkarıldı.")
# for öngüsü ile listenin elemanlarını sırayla ekrana yazdıralım
for i in range(len(names)):
    print(f"{i + 1}. {names[i].upper()}")
```

<h4>TUPLE (ELEMANLARI DEĞİŞTİRİLEMEYEN LİSTE - IMMUTABLE LIST)</h4>

<p align="justify">Listelerin elemanlarını yeniden atayabildik ve hatta istediklerimizi silebildik. Burada ismi geçen <b>TUPLE</b> veri yapısında ise elemanları değiştiremiyoruz (immutable). Ancak aynı isimle yeniden bir <b>TUPLE</b> tanımlayabiliyoruz. <b>TUPLE</b> veri yapısı bazen bir satırda birden fazla değişken atamak için kullanılarak yer kazandırdığından bu yapıyı sık sık tercih ediyoruz.</p>

<b>tuple_example.py</b>

```
COLOR = (255, 255, 255) # beyaz renk kodu
# COLOR isimli TUPLE'ın elemanlarını değiştirmeye çalışalım
COLOR[0] = 0 # hata verecektir
# COLOR isimli TUPLE'ı yeniden tanımlayalım
COLOR = (0, 0, 0) # siyah renk kodu
# üç farklı değişkeni aynı satırda atayalım
age, name, weight = 21, "Furkan", 70.3
print(f"age = {age}, name = {name}, weight = {weight}")
print(f"type(age) = {type(age)} type(name) = {type(name)} type(weight) = {type(weight)}")
print(f"type(age, name, weight) = {type((age, name, weight))}")
```