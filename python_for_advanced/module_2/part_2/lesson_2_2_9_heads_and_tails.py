"""
Орел и решка
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла,
а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее
количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 00.
"""

text = input()
biggest_counter = 0
tmp_counter = 0
for c in text:
    if c == "Р":
        tmp_counter += 1
    if c == "О":
        tmp_counter = 0
    if tmp_counter > biggest_counter:
        biggest_counter = tmp_counter
print(biggest_counter)