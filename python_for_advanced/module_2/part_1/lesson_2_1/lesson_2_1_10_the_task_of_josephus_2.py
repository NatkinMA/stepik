"""
Задача Иосифа Флавия
n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться,
каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего
за ним человека. Напишите программу, определяющую номер человека, который останется
в кругу последним.

Формат входных данных
На вход программе подаются два числа n и k, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.
"""

def joseph(n, k):
    if n == 1:
        return 1
    if n > 1:
        return (joseph(n - 1, k) + k - 1 ) % n + 1

n = int(input())
k = int(input())

print(joseph(n, k))