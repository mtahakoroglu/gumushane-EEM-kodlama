names = ["Abdullah", "sefa", "selin", "cindy", "patrick", "SAFA", "destinee"] # Bir Python listesi
print(f"names = {names}")
print(f"names isimli listenin uzunluğu {len(names)}.")
# Listede bulunan isimlerden baş harfi 'S' olanların sayısını bulalım
s_count = 0
for name in names:
    if name[0].upper() == 'S':
        s_count += 1
print(f"Listede bulunan isimlerden baş harfi 'S' olanların sayısı {s_count}.")