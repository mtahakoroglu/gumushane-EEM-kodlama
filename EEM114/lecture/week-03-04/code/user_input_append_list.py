names = [] # boş bir liste
k = 0 # listedeki isim sayısını bir indeks ile kendimiz hesaplayalım
while True: # sonsuz döngü
    secim = int(input("İsim eklemek için 1'e, programı sonlandırmak için 2'ye basınız: "))
    if secim == 1:
        name = input("İsim giriniz: ")
        names.append(name)
        k += 1
    elif secim == 2:
        break
    else:
        print("Hatalı giriş yaptınız!")
print(f"İsim listesi = {names}")
print(f"Listede toplam {k} isim var.")
print(f"Listedeki isim sayısı {len(names)}.")