"""
Конкатенация файлов 🌶️
На вход программе подается натуральное число n и n строк с названиями файлов.
Напишите программу, которая создает файл output.txt и выводит в него содержимое
всех файлов с указанными именами, не меняя их порядка.

Формат входных данных
На вход программе подается натуральное число n и n строк названий существующих файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
"""

with open('output.txt', 'w', encoding='utf-8') as output_file:
    n = int(input())
    for _ in range(n):
        with open(input(), 'r', encoding='utf-8') as file:
            output_file.write(file.read())
