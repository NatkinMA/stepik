from random import *

DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_"

chars = ""


def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password = password + choice(chars)
    return password


cntPw = int(input('Укажите количество паролей для генерации:'))
lenPw = int(input('Укажите длину одного пароля:'))
digOn = input('Включать ли цифры 0123456789? (y/n)')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

if digOn.lower() == 'y':
    chars += DIGITS
if abcOn.lower() == 'y':
    chars += LOWERCASE_LETTERS
if ABCon.lower() == 'y':
    chars += UPPERCASE_LETTERS
if chOn.lower() == 'y':
    chars += PUNCTUATION
if excOn.lower() == 'y':
    for c in 'il1Lo0O':
        chars.replace(c, '')

for _ in range(cntPw):
    print(generate_password(lenPw, chars))
