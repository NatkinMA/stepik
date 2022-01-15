"""
Угадайка слов
Описание проекта: программа загадывает слово, а пользователь должен его угадать.
Изначально все буквы слова неизвестны. Также рисуется виселица с петлей. Пользователь
предлагает букву, которая может входить в это слово. Если такая буква есть в слове,
то программа ставит букву столько раз, сколько она встречается в слове. Если такой буквы нет,
к виселице добавляется круг в петле, изображающий голову. Пользователь продолжает отгадывать
буквы до тех пор, пока не отгадает всё слово. За каждую неудачную попытку добавляется
еще одна часть туловища висельника (обычно их 6: голова, туловище, 2 руки и 2 ноги.
"""

from random import *

word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история",
             "женщина", "развитие", "власть", "правительство", "начальник", "спектакль",
             "автомобиль", "экономика", "литература", "граница", "магазин", "председатель",
             "сотрудник", "республика", "личность"]

def get_word():
    return word_list[randint(0, len(word_list) - 1)].upper()

def print_word(word, list):
    for c in word:
        if c in list:
            print(c, end=" ")
        else:
            print("_", end=" ")
    print()

def display_hagman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print("Давайте играть в угадайку слов!")
    display_hagman(tries)
    print(word_completion)

    while True:
        word_input = input("Введите букву или слово: ").upper()
        if not word_input.isalpha():
            print("Вы ошиблись, попробуйте еще!")
            continue
        if word_input in guessed_words or word_input in guessed_letters:
            print("Уже было")
            continue
        if len(word_input) > 1:
            if word_input == word:
                print("Поздравляем, вы угадали слово! Вы победили!")
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(f"Не верно, осталось попыток {tries}")
                print(display_hagman(tries))
                print(word, guessed_letters)
                if tries == 0:
                    print(f"Вы не смогли угадать слово: {word}")
                    break
                continue

        if word_input in word:
            guessed_letters.append(word_input)
            for c in word:
                if c not in guessed_letters:
                    print("Угадали букву")
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:
                print_word(word, guessed_letters)
                print("Поздравляем, вы угадали слово! Вы победили!")
                break
        else:
            guessed_letters.append(word_input)
            tries -= 1
            print(f"Не верно, осталось попыток {tries}")
            print(display_hagman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f"Вы не смогли угадать слово: {word}")
            break

while True:
    play(get_word().upper())
    wanna_play = input("Хотите сыграть еще раз(y/n)? ").upper()
    if wanna_play == "Y":
        continue
    else:
        break
