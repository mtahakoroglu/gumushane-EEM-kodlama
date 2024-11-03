<h3>LİSTELERLE ÇALIŞMAK (WORKING with LISTS)</h3>

<h4>YEREL KLASÖRÜ GÜNCELLEME</h4>
<p align="justify">6. ve 7. haftada yaptığımız işleri bilgisayarınızda kendiniz yaparak dersin hocası ile aynı yere gelebilirsiniz. Ya da PowerShell ile "gumushane-EEM-bilgisayar-programlama" klasörünüzün bulunduğu dizine giderek</p>

```
git pull
```

<p align="justify">komutuyla "gumushane-EEM-bilgisayar-programlama" yerel klasörünüzü güncelleyebilirsiniz. İlgili videoyu <a href="https://youtu.be/q27HubmtPhc">izleyin</a>.</p>


<h4>KARIŞIK LİSTE</h4>
<p align="justify">Şu ana kadar (4. ve 5. haftalarda) elemanları string, integer, float veya bool veri tipi olan listelerle çalıştık. Şimdi elemanları karışık veri tipleri olan hatta bir elemanı liste bile olabilen bir liste oluşturalım. İlgili videoyu izlemek için <a href="youtube.com">tıklayınız</a>.</p>

<b>mixed_list.py</b>

```
mixed_list = ["Sefa", 21, 64.1, True]
print(f"mixed_list = {mixed_list}")
mixed_list.append(["Patrick", 22, 67.3, False])
print(f"mixed_list = {mixed_list}")
```
