import random

DIGITS = ['0123456789', False]
LOWERCASE_LETTERS = ['abcdefghijklmnopqrstuvwxyz', False]
UPPERCASE_LETTERS = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', False]
PUNCTUATION = ['!#$%&*+-=?@^_', False]
BADCHARS = ['il1Lo0O', False]
allchars = ''

def answer(t):
    print(t)
    while True:
        t = input().lower()

        if t == 'да':
            return True

        elif t == 'нет':
            return False

p_counter = int(input('Введите количество генерируемых паролей'))

for i in range(p_counter):
    p_len = int(input('Введите длину пароля'))

    if answer('Включать ли цифры', DIGITS, 'в возможную область генерации?'):
        DIGITS[1] = True
    if answer('Включать ли прописные буквы', UPPERCASE_LETTERS, 'в возможную область генерации?'):
        UPPERCASE_LETTERS[1] = True
    if answer('Включать ли строчные буквы', LOWERCASE_LETTERS, 'в возможную область генерации?'):
        LOWERCASE_LETTERS[1] = True
    if answer('Включать ли символы', PUNCTUATION, 'в возможную область генерации?'):
        PUNCTUATION[1] = True
    if answer('Исключать ли неоднозначные символы', BADCHARS, 'в возможную область генерации?'):
        BADCHARS[1] = True