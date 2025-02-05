import numpy as np

def circle_perimeter_area(radius):
    perimeter = 2 * np.pi * radius
    area = np.pi * radius ** 2
    return perimeter, area

r = float(input("Çemberin yarıçapını giriniz: "))
p, a = circle_perimeter_area(r)

print(f"Yarıçapı {r} olan çemberin çevresi {p:.2f}, alanı {a:.2f}'dir.")