import re

# re.match()  #соответствие начала строки шаблону, если находит значение то возвращает его, если нет, то None
# re.search() # поиск в строке
# re.findall() #сколько объектов удовлетворяет, возвращает количество и список
# re.split() #разделение по шаблонам
# re.sub() # замена наших объектов на что-то другое
# re.compile() #охраняем паттерн в переменную и ее применяем

import re
result = re.match(r"AV", "AV Analytics Vidhya AV")
print(result)

result = re.match(r"(AV)(34)", "AV34 Analytics Vidhya AV")
print(result.group(1))

result = re.match(r"Analytics", "AV Analytics Vidhya AV")
print(result) #None - т.к. ищет в начале строки

result = re.match(r"AV", "AV Analytics Vidhya AV")
print(result)
print(result.start())
print(result.end())

result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print(result) #span начинается с индекса 3
print(result.group(0))
print(result.start())

result = re.findall(r'AV|XY|34', 'AV Analytics XY Vidhya AV 34')
print(result)


result = re.split(r" ", "Hello, world!")
print(result)

result = re.split(r"\*\*\*", "Hello***world!")
print(result)

result = re.split(r"[abc]34", "Hello a34 world b34 asdf!")
print(result)

result = re.sub(r"India", "the World", "AV is largest Analytics community of India")
print(result)

result = re.sub(r"[abc][123]{2,3}|[India]]", "the World", "AV is b333 largest Analytics community of India")
print(result)

pattern = re.compile("AV")
result = pattern.findall("AV Analytics Vidhya AV")
print(result)
result2 = pattern.findall("AV is largest analytics community of India")
print(result2)

# . - Один любой символ, кроме новой строки \n.
# ? - 0 или 1 вхождение шаблона слева
# + - 1 и более вхождений шаблона слева
# * - 0 и более вхождений шаблона слева
# \w - Любая цифра или буква (\W — все, кроме буквы или цифры)
# \d - Любая цифра [0-9] (\D — все, кроме цифры)
# \s - Любой пробельный символ (\S — любой непробельный символ)
# \b - Граница слова
# [..] - Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# \ - Экранирование специальных символов (. означает точку или + — знак «плюс»)
# ^ и $ - Начало и конец строки соответственно
# {n,m} - От n до m вхождений ({,m} — от 0 до m)
# a|b - Соответствует a или b
# () - Группирует выражение и возвращает найденный текст
# \t, \n, \r - Символ табуляции, новой строки и возврата каретки соответственно
# Больше информации по специальным символам, таким как (), |


result = re.findall(r'[;:]\-*[\(\)\[\]\]]+', 'asdf :-)  asdff ;-))) asdf :[[[[[ asdfasdf :-]]))')
print(result)

result = re.findall(r'[;:]\-*[\(\)]+|[;:]\-*[\[\]]+', 'asdf :-)  asdff ;-))) asdf :[[[[[ asdfasdf :-]]))')
print(result)

result = re.findall(r'[;:]\-*[\(\)]+|[;:]\-*[\[\]]+', ':);------[[[[[]')
print(len(result))
print(result)


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed=breed

sharik = Dog('Sharik','Bulldog', 10)
bob = Dog('Bobik', 'pudle', 7)
print(sharik.name)
print(bob.age)

