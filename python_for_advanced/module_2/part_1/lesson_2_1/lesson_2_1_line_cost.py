'''
Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того,
что один любой символ (в том числе пробел) стоит 6060 копеек. Ответ дайте в рублях
и копейках в соответствии с примерами.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести стоимость строки.
'''

text = input()
cost = len(text) * 60
print("{} р. {} коп.".format(cost // 100, cost % 100))
