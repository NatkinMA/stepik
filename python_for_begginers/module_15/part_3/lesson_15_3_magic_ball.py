from random import *

answers = ["Бесспорно", "Предрешено", "Никаких сомнений",
           "Определенно да", "Можешь быть уверен в этом",
           "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы",
           "Знаки говорят - да", "Да",
           "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать",
           "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять",
           "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
           "Перспективы не очень хорошие", "Весьма сомнительно"]

def choice(answers):
    return answers[randint(0, 19)]


def one_more_question():
    while True:
        print("Хочешь задать еще один вопрос (да/нет)?")
        user_answer = input().lower()
        if user_answer != "да" and user_answer != "нет":
            print("Введите корректный ответ на вопрос: 'да' или 'нет'.")
            continue
        elif user_answer == "да":
            return True
        elif user_answer == "нет":
            return False


print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")

print("Как тебя зовут?")
user_name = input()
print("Привет {}!".format(user_name))

while True:
    print("Введи свой вопрос: ", end="")
    question = input()
    print(choice(answers))
    if one_more_question():
        continue
    else:
        print("Возвращайся если возникнут вопросы!")
        break
