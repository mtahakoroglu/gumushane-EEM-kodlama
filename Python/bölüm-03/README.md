<h3>LİSTELERE GİRİŞ (INTRODUCING LISTS)</h3>
<p align="justify">Bu bölümde listelere bakmaya başlıyoruz. Listelere ait bir metot olan <b>append()</b> ile kullanıcının direkt konsoldan klavye ile oluşturduğu dinamik (yâni uzunluğu kullanıcıya bağlı olan, önceden belli olmayan) bir kişiler listesi oluşturalım. İlgili videoyu yakında <b>buradan</b> izleyebilirsiniz.</p>


<b>people_list_console_input.py</b>

```
name = []
while True:
    choice = int(input("Bir kişi ismini listeye eklemek için için 1, listeyi sonlandırmak için 2 giriniz: "))
    if choice == 1:
        name.append(input("Bir kişi ismi girin: "))
    elif choice == 2:
        break
    else:
        print("Yanlış giriş! Tekrar seçim yapın.")
print(f"Listeyi sonlandırdınız. Liste toplam {len(name)} kişiden oluşmaktadır ve aşağıdaki gibidir.")
print(name)
```