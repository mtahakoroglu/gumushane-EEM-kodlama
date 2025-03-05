<h3>LİSTELERLE ÇALIŞMA (WORKING w/ LISTS)</h3>

<h4>KARIŞIK LİSTE</h4>
<p align="justify">Şu ana kadar (3. ve 4. haftalarda) elemanları string, integer, float veya bool veri tipi olan listelerle çalıştık. Şimdi elemanları karışık veri tipleri olan hatta bir elemanı liste bile olabilen bir liste oluşturalım. İlgili videoyu izlemek için <a href="https://www.youtube.com/watch?v=yUcQvadgCrc">tıklayınız</a>. Videonun sonunda <b>mixed_list</b> isimli karışık listenin sonuna eklediğimiz listenin üçüncü elemanı olan 67.3'e <b><i>mixed_list[-1][2]</i></b> şeklinde eriştik.</p>

<b>mixed_list.py</b>

```
mixed_list = ["Muhammed", 19, 85.4, True]
mixed_list.append(["Eray", 20, 67.3, False])
print(f"mixed_list = {mixed_list}")
print(f"mixed_list[0] = {mixed_list[0]}")
print(f"type({mixed_list[0]}) = {type(mixed_list[0])}")
print(f"mixed_list[1] = {mixed_list[1]}")
print(f"type({mixed_list[1]}) = {type(mixed_list[1])}")
print(f"mixed_list[2] = {mixed_list[2]}")
print(f"type({mixed_list[2]}) = {type(mixed_list[2])}")
print(f"mixed_list[3] = {mixed_list[3]}")
print(f"type({mixed_list[3]}) = {type(mixed_list[3])}")
print(f"mixed_list[4] = {mixed_list[4]}")
print(f"type({mixed_list[4]}) = {type(mixed_list[4])}")
# listenin son elemanı olan listede 67.3'e erişmek istiyoruz
print(f"mixed_list[-1][2] = {mixed_list[-1][2]}")
```