from random import *

flag = True
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
BADCHARS = ['il1Lo0O', False]
allchars = ''

def answer():
    while True:
        a = input().lower()

        if a == 'да':
            return True

        elif a == 'нет':
            return False

def generate_password(chars, length):
    password = ''
    if len(chars) <= 0 or length <= 0:
        return '0'
    for i in range(length):
        char = choice(chars)
        if BADCHARS and char not in BADCHARS:
            password += char
        else:
            i += -1
    return password

p_counter = int(input('Введите количество генерируемых паролей '))

for i in range(p_counter):
    if flag:
        p_len = int(input('Введите длину пароля '))

        print('Включать ли цифры', DIGITS, 'в возможную область генерации?')
        if answer():
            allchars += DIGITS
        print('Включать ли прописные буквы', UPPERCASE_LETTERS, 'в возможную область генерации?')
        if answer():
            allchars += UPPERCASE_LETTERS
        print('Включать ли строчные буквы', LOWERCASE_LETTERS, 'в возможную область генерации?')
        if answer():
            allchars += LOWERCASE_LETTERS
        print('Включать ли символы', PUNCTUATION, 'в возможную область генерации?')
        if answer():
            allchars += PUNCTUATION
        print('Исключать ли неоднозначные символы', BADCHARS[0], 'в возможную область генерации?')
        if answer():
            BADCHARS[1] = True
        flag = False
    print('Ваш пароль', generate_password(allchars, p_len))