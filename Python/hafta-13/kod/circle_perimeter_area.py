import numpy as np
r = float(input("Çemberin yarıçapını giriniz: "))
perimeter = 2*np.pi*r
area = np.pi*r**2
print(f"Yarıçapı {r} olan çemberin çevresi {perimeter:.2f}, alanı {area:.2f}'dir.")