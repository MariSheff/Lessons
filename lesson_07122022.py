# # КЛАССЫ
# class Dog:
#     # Class attribute
#     species = "Canis familiaris"
#
#     def __init__(self, name, breed, age, weight):
#         self.name = name
#         self.age = age
#         self.breed=breed
#         self.weight = weight
#         self.status = 'Hungry'
#         self.last_meal = 'Nothing'
#
#     def feed(self, meal, mass):
#         print(self.name, 'has been fed')
#         self.weight += mass
#         self.status = 'not hungry'
#         self.last_meal = meal
#
#     def groom(self):
#         print('Thanks')
#         self.feed('some_meal', 0.1)
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old. \nHe/she is {self.status} ang weights {self.weight} kilos."
#
#     def __repr__(self):
#         return f"{self.name} is {self.age} years old.\nHe/she is {self.status} ang weights {self.weight} kilos."
#
#     def speak(self,sound):
#         return f'{self.name} says {sound}'
#
# sharik = Dog('Sharik','Bulldog', 10, 20)
# bobik = Dog('Bobik', 'pudle', 7, 10)
#
# print(sharik.name)
# print(bobik.name)
#
# sharik.feed('beef', 0.2)
# print(sharik.weight)
# print(sharik.status)
# print(sharik.last_meal)
#
# bobik.feed('cheese', .1) #0.1 можно писать как .1
# print(bobik.weight)
# print(bobik.status)
# print(bobik.last_meal)
#
# bobik.groom()
#
# print(sharik.species)
#
# # bobik.species = 'Unknown!'
# # print(bobik.species)
#
# Dog.species = 'AAAAAAA'
# print(Dog.species)
# print(bobik.species)
# print(sharik.species)
#
# #Питон позволяет создать атрибуты у объекта и класса на ходу, данная возможность крайне нежелательна к использованию
#
# Dog.speed = 20
# print(Dog.speed)
#
# # print(dir(sharik))
# print(sharik)  # тоже самое print(sharik.__str__()), но сначала надо переписать __str__ у класса Dog.
# # print(sharik.__str__())
#
# del bobik #удаление объекта
#
# print(sharik)
# print(sharik.speak('RRrrrrr'))
#
# # class Car:
# #
# #     def __init__(self, model, miliage, color):
# #         self.model = model
# #         self.miliage = miliage
# #         self.color = color
# #
# #     def drive(self, dist):
# #         self.miliage += dist
# #
# #
# # lada = Car('Lada', 100, 'white')
# # mers = Car('Mers', 200, 'red')
# # bmw = Car('BMW', 300, 'black')
# #
# # lada.drive(50)
# # print(lada.miliage)
#
#
# # НАСЛЕДОВАНИЕ, super()
#
# class Dog:
#     species = "Canis familiaris"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} barks: {sound}"
#
# # class JackRussellTerrier(Dog):
# #     pass
#
# class JackRussellTerrier(Dog): # Полиморфизм
#     # def speak(self, sound='Arf'):
#     #     return f"{self.name} says {sound}"
#     def speak(self, sound='Arf'):
#         return super().speak(sound) #использование функции родителя класса с передачей значения по умолчанию
#
# class Bulldog(Dog):
#     pass
#
# class Dachshund(Dog):
#     pass
#
#
# miles = JackRussellTerrier("Miles", 4)
# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)
#
#
# print(miles.species)
#
# print(buddy.name)
#
# print(jack)
# print(jim.speak("Woof"))
# print(miles.speak())
# print(isinstance(miles, Dog))

### MORE ABOUT SUPER()

#Было неэффективною т.к. дважды прописываем функции для квадрата и прямоугольника
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

square = Square(4)
print(square.area())

rectangle = Rectangle(2,4)
print(rectangle.area())

#Стало эффективно с использованием супер()
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * self.length + 2 * self.width
#
# # Here we declare that the Square class inherits from the Rectangle class
# class Square(Rectangle):  #наследование
#     def __init__(self, length):
#         super().__init__(length, length) #super()
#
#
# square1 = Square(5)
# print(square1.area())

#вводим отдельный класс Куб, который наследуется от класса Квадрат
# class Cube(Square):
#     def surface_area(self):
#         face_area = super().area()
#         return face_area * 6
#
#     def volume(self):
#         face_area = super().area()
#         return face_area * self.length

# cube1 = Cube(5)
# print(cube1.surface_area())
# print(cube1.volume())
# print(Cube.__mro__) #порядок классов, которые возникают при поиске методов (класс Куб от класса Квадрат от класса Прямоугольник)

# A super() DEEP DIVE
#
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()  # лучше избегать такого написания
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length
#
# cube1 = Cube(5)
# print(cube1.surface_area())
# print(cube1.volume())

'''
The parameterless call to super() is recommended and sufficient for most use cases, 
and needing to change the search hierarchy regularly could be indicative of a larger design issue.
'''

#МНОГО РОДИТЕЛЕЙ. Множественное наследование:

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)  #__init__ первого родителя Square, передаем self.base - сторона квадрата

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

print(RightPyramid.__mro__)
pyramid = RightPyramid(2, 4)
print(pyramid.area())
print(pyramid.perimeter())

# ДАТА КЛАССЫ

from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts1 = DataClassCard('Q', 'Hearts')
print(queen_of_hearts1.rank)
queen_of_hearts2 = DataClassCard('Q', 'Hearts')
print(queen_of_hearts2.rank)

print(queen_of_hearts1 == queen_of_hearts2)
print(queen_of_hearts2)


from collections import namedtuple
NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])

queen_of_hearts = NamedTupleCard('Q','Hearts')
print(queen_of_hearts == ('Q', 'Hearts'))


#Default Values
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

p1 = Position('my_position')
print(p1.lon)
print(p1.lat)