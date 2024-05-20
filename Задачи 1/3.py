import string

str = str(input('Введите строку: '))

str = str.lower()
str = str.replace(' ', '')
for i in string.punctuation:
    str = str.replace(i, '')

if str == str[::-1]:
    print('Эта строка - палиндром')
else:
    print('Эта строка - не палиндром')
