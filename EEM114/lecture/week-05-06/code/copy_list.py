numbers = [3, 5, 78, -23, 6, -8]
numbers2 = numbers
numbers.append(10)
print(f"numbers = {numbers}")
print(f"numbers2 = {numbers2}")
# iki liste ismi de aynı listeyi gösteriyor.
# bunu istemiyoruz. listeyi kopyalayalım.
numbers = [3, 5, 78, -23, 6, -8]
numbers2 = numbers[:]
numbers.append(10)
print(f"numbers = {numbers}")
print(f"numbers2 = {numbers2}")
# şimdi numbers2 listesi numbers listesinin kopyası oldu.
# ikinci yol olarak bir lite metodu olan copy() metodunu kullanabiliriz.
numbers = [3, 5, 78, -23, 6, -8]
numbers2 = numbers.copy()
numbers.append(10)
print(f"numbers = {numbers}")
print(f"numbers2 = {numbers2}")