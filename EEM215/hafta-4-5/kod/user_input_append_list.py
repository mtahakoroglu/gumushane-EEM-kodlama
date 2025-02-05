names = []

k = 0 # listeye eklenen isimleri kendimiz sayalım
while True:
    s = int(input("İsim eklemek için 1'e, programı sonlandırmak için 2'a basınız: "))
    if s == 1:
        names.append(input("İsim giriniz: "))
        k += 1 # k = k+1
    elif s == 2:
        print("Program sonlandırıldı.")
        break
    else:
        print("Hatalı giriş yaptınız! Lütfen tekrar deneyiniz.")

print(f"names = {names}") # isimler listesi
print(f"names isimli listenin uzunluğu: {len(names)}") # isimler listesinin uzunluğu
print(f"names isimli listenin kendi sayımımıza göre uzunluğu: {k}") # isimler listesinin uzunluğu