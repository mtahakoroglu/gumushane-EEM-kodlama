<h3>SÖZLÜKLER (DICTIONARY)</h3>

<h4>Öğrenci Notları Sözlüğü</h4>

<p align="justify">İlgili video için <a href="https://www.youtube.com">tıklayınız</a>.</a>

<b>student_grades_dictionary.py</b>

```
# Öğrenci notlarını içeren sözlük
studentGrades = {
    "Ayşe": 85,
    "Mehmet": 92,
    "Fatma": 78,
    "Ali": 88,
    "Zeynep": 95
}

# Fonksiyon: Ortalama notu ve en yüksek notu alan öğrenciyi hesaplar
def dictionary_stats(gradesDict):
    grades = list(gradesDict.values())
    average = sum(grades) / len(grades)
    maxGrade = max(grades)
    maxGradeIndex = grades.index(maxGrade)
    bestGuy = list(gradesDict.keys())[maxGradeIndex]
    return average, bestGuy

# Sözlüğü yazdır
print(f"Öğrenci Notları Sözlüğü: {studentGrades}")
# Fonksiyonu çağır
averageGrade, bestStudent = dictionary_stats(studentGrades)
# Sonuçları yazdır
print(f"Sınıfın not ortalaması: {averageGrade:.2f}")
print(f"En yüksek notu alan öğrenci {bestStudent} olup {studentGrades[bestStudent]} almıştır.")
```