# Öğrencinin notlarını konsol (terminal) ekranında kullanıcıdan isteyiniz
vize = float(input("Vize sınav notunuzu girin: "))
final = float(input("Final sınav notunuzu girin: "))
# Ortalama notu hesapla: Vize notunun etkisi %40, final notunun etkisi %60
ortalama = round((vize * 0.4) + (final * 0.6))
# Geçiş notları ve harf notları
not_gecis = [81, 76, 70, 60, 50, 45, 30, 0]
harf_notlari = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FD", "FF"]
harfNotu = "" # Aşağıda döngüde harf notunu hesaplayacağımızdan dolayı burada tanımla
for i in range(len(not_gecis)): # Döngü ile harf notunu belirle
    if ortalama >= not_gecis[i]:
        harfNotu = harf_notlari[i]
        break # ortalama notun yer aldığı aralığı bulduğumuz zaman döngüyü sonlandır
# Sonucu konsol (terminal) ekranına yazdır
print(f"Ortalamanız: {ortalama:.2f} --> Harf notunuz: {harfNotu}")
