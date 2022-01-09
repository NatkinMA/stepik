
def caesar_shift(char, step, lang):
    ALPHABETS = ["АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    result = ""
    if char.isalpha():
        result = ALPHABETS[lang][(ALPHABETS[lang].index(char.upper()) + step) % len(ALPHABETS[lang])]
    return result if char.isupper() else result.lower()


direction = input("Выберите направление: \n(+) - Шифрование \n(-) - Дешифрование:\n ")
lang = int(input("Выбери язык алфавита: \n0 - Русский \n1 - Английский: \n "))
#step = int(direction + input("Введи число, шаг сдвига (со сдвигом вправо): "))
text = input("Введите текст для обработки:\n")
for i in range(26):
    for c in text:
        if c.isalpha():
            print(caesar_shift(c, int(direction + str(i)), lang), end="")
        else:
            print(c, end="")
    print()
