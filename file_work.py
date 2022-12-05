f = open("text1.txt", 'rt', encoding='UTF-8')

print(f.read(5))  #читает первые 5 строк
position = f.tell()
print(position)   #указывает накаком символе стоим
print(f.read(5))  #читает следующие 5 строк
f.seek(position+3)  #перевод курсора на 3 символа вперед
print(f.read(4))  #читает след.4 символа и так далее

print(f.readline())   #чтение построчно
print(f.readlines(1)) #чтение всех строк в одну или построчно с указанием строки

for line in f:
    print(line)

f = open("new_text.txt", "wt")

f.write("New string\n")
f.write("Another string\n")

f.close()

f = open("new_text2.txt", "wt")

lines = [
f.write("New string\n"),
f.write("Another string\n")
]

f.close()
### ДОЗАПИСЬ
f = open("new_text3.txt", "a")

lines = [
f.write("New string\n"),
f.write("Another string\n")
]

f.close()


obj = b"Hello, world!"
# obj = b"Hello\x0D\x0A\x41\x00"
print(obj)



f = open("data.dat", "wb")

f.writelines([b"A", b"\n"])
f.write(b"23")

f.close()
f = open("data.dat", "rb")

print(f.read())

f.close()

with open("newfile.txt", "w", encoding="utf-8") as f:
    d = int(input())
    f.write("1 / {} = {}".format(d, 1 / d)) #аналог написания f-string


import pickle

obj = {"one": 123, "two": [1, 2, 3]}
output = pickle.dumps(obj, 2)
new_obj = pickle.loads(output)

print(obj)
print(new_obj)

import pickle

obj = {"one": 123, "two": [1, 2, 3]}
with open("data.pkl", "wb") as f:
    pickle.dump(obj, f, 2)

with open("data.pkl", "rb") as f:
    new_obj = pickle.load(f)
print(new_obj)

import json

obj = {"one": 123, "two": [1, 2, 3]}
output = json.dumps(obj)
new_obj = json.loads(output)

print(new_obj)

import json
import re

obj = {"one": 123, "two": [1, 2, 3],
       'three': {"a": 123, "b": [1, 2, 3]}}
with open("data.json", "wt") as f:
    json.dump(obj, f, indent=4) # indent=4 отступы от края

with open("data.json", "rt") as f:
    obj1 = json.load(f)

print(obj1)


#РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
import re

match = re.search(r'tea:[abc]+4', 'Hello tea:aaa4')  # результат выводит span=(6,14) - место откуда до куда найден текст
print(match)