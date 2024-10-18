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