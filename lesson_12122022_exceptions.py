# Отслеживание ошибок:
# Try - except (Попытка - Исключение) для предупреждения фатальных ошибок
try:
    x = int(input("Введите число: "))
    x +=5
    print(x)
except ValueError:
    print("Нужно ввести число!")

try:

    x = int(input("Введите число: "))
    a = 5/x
except ZeroDivisionError:
    print('Деление на ноль!')
except ValueError:
    print("Введите число!!!")
# else:                            #необязательное написание
#     print("Иначе")
# finally:                         #необязательное написание
#     print("Finelly")