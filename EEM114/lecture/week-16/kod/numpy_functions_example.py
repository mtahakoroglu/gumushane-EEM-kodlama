from numpy.random import randint

# -20 ile 20 arasında 10 tane rastgele sayı üret
numbers = randint(-20, 21, 10)
print("Rastgele sayılar:", numbers)

# sayı dizisindeki pozitif sayılardan oluşan yeni bir dizi üreten fonksiyon
def get_positive_numbers(numbers):
    positive_numbers = numbers[numbers > 0]
    return positive_numbers

positiveNumbers = get_positive_numbers(numbers)
print("Pozitif sayılar:", positiveNumbers)