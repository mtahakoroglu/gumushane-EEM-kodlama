numbers = [2, 7, -8, 12, 5, -34, 56, 15, -3] # Bir Python listesi
print(f"numbers = {numbers}")
print(f"numbers isimli listenin uzunluğu {len(numbers)}.")
# numbers isimli listenin elemanlarını dolaşarak negatif eleman sayısını bulalım
count = 0
for number in numbers:
    if number < 0:
        count += 1
print(f"numbers isimli listenin içinde {count} tane negatif sayı var.")