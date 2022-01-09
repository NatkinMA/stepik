
def caesar_shift(char, step):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    if char.isalpha():
        result = ALPHABET[(ALPHABET.index(char.upper()) + step) % len(ALPHABET)]
    else:
        result = char
    return result if char.isupper() else result.lower()

def caesar_shift_word(word):
    PUNCTUATION = "!#$%&*+-=?@^_\",.,."
    word_without_punctuation = ""
    for c in word:
        if c not in PUNCTUATION:
            word_without_punctuation = word_without_punctuation + c
    lenght_of_word = len(word_without_punctuation)
    result = ""
    for c in word:
        result = result + caesar_shift(c, lenght_of_word)
    return result

text = input().split()

for i in range(len(text)):
    text[i] = caesar_shift_word(text[i])

print(" ".join(text))
