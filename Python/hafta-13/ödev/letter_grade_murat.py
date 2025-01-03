# Öğrencinin notlar
vize = float(input("Vize sınav notlarıunu gir: "))
final = float(input("Final sınav notlarıunu gir: "))

# Ortalama hesapla
ortalama = round((vize * 0.4) + (final * 0.6))
# Not aralıklar ve harf notlar
not_araliklar = [90, 81, 76, 70, 60, 50, 45, 30, 0]
harf_notlar = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FD", "FF"]

# Döngü ile harf notunu belirle
harf_notu = ""
for i in range(len(not_araliklar)):
    if ortalama >= not_araliklar[i]:
        harf_notu = harf_notlar[i]
        break

# Sonuç
print(f"Ortalamanız: {ortalama:.2f}")
print(f"Harf notunuz: {harf_notu}")