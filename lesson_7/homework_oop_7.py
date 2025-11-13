# import datetime
#
# """1. Создай три класса: Cat, Dog, Duck.
# В каждом реализуй метод speak(), возвращающий уникальную строку.
# Создай список из экземпляров этих классов и вызови метод speak()
# в цикле."""
# class Cat:
#     def speak(self, text):
#         print (f"Кошка говорит {text}")
# class Dog:
#     def speak(self, text):
#         print(f"Собака говорит {text}")
# class Duck:
#     def speak(self, text):
#         print(f"Утка говорит {text}")
#
# animals = [Cat(), Dog(), Duck()]
# for animal in animals:
#     animal.speak("текст")
#
# """2. Создай базовый класс Shape
# Создай три класса-наследника: Square, Rectangle, Triangle,
# в каждом реализуй метод get_pr().
# Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
# можно обойти в цикле и вызвать get_pr() у каждого."""
# class Shape:
#     def get_pr(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def get_pr(self):
#         return f"Периметр квадрата со стороной {self.side} = {self.side * 4}"
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_pr(self):
#         return f"Периметр прямоугольника со сторонами {self.width} и {self.height} = {2 * (self.width + self.height)}"
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_pr(self):
#         return f"Периметр треугольника со сторонами {self.a}, {self.b}, {self.c} = {self.a + self.b + self.c}"
#
# shapes = [Square(5),Rectangle(5, 6),Triangle(3, 4, 5)]
#
# for shape in shapes:
#     perimeter = shape.get_pr()
#     print(perimeter)
#
# """3. Сделай класс Shape абстрактным.
# Переопредели get_pr() как @abstractmethod.
# Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError."""
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def get_pr(self):
#         pass
#
# try:
#     test = Shape()
# except TypeError as e:
#     print("!Словили TypeError!")
# else:
#     print("Не словили TypeError")
#
# """4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
# Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
# Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы."""
# class A:
#     def __init__(self):
#         super().__init__()
#         print("init A")
# class B:
#     def __init__(self):
#         super().__init__()
#         print("init B")
# class C:
#     def __init__(self):
#         super().__init__()
#         print("init C")
#
# class D(A, B, C):
#     def __init__(self):
#         super().__init__()
#         print("init D")
# print(D.__mro__)
# d = D()
#
# """5. Создай MixinLog (как в уроке).
# Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
# Создай класс, который наследует оба класса. Создай экземпляр этого класса."""
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id} продан в {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#
# class Booking:
#     def __init__(self, room, guests):
#         super().__init__()
#         self.room = room
#         self.guests = guests
#
#     def print_info(self):
#         print(f"Комната {self.room}, гостей - {self.guests}")
#
# class Resp(Booking, MixinLog):
#     pass
#
# r = Resp(343, 4)
# # r.print_info()
# # r.save_sell_log()
#
#
# """6. В Goods и MixinLog реализуй print_info().
# Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
# Измени порядок наследования — изменилась ли логика?"""
#
# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"Goods.print_info: {self.name}, {self.price}, {self.weight}")
#
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def print_info(self):
#         print(f"MixinLog.print_info: ID={self.id}")
#
#     def save_sell_log(self):
#         print(f"{self.id} продан в {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
# print(Notebook.__mro__)
# class Notebook(MixinLog, Goods):
#     pass
# print(Notebook.__mro__) #порядок изменился
#
# """Далее задания можете сделать через классы, функции или без них."""
#
# """7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
# Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
# и выведи сообщение: "На ноль делить нельзя!"""
# """8. Расширь программу из Задания 1:
# Добавь обработку ошибки (как называется ошибка найди сам),
# если пользователь ввёл не числа, а текст.
# Выведи сообщение: "Ошибка ввода: введите два числа через пробел"""
# """9. Модифицируй код так, чтобы после обработки конкретных ошибок
# был ещё один общий except, который перехватывает все остальные ошибки и выводит:
# "Произошла неизвестная ошибка"""
# """10. При перехвате исключений из 7 и 8 заданий,
# сохрани ошибку в переменную e и выведи её текст:"""
#
#
# input_num = input("Введите два числа через пробел: ")
#
# numbers = input_num.split()
#
# try:
#     if len(numbers) != 2:
#         raise ValueError("Нужно ввести два числа!")
#     num_1, num_2 = float(numbers[0]), float(numbers[1])
#     res = num_1 / num_2
# except ValueError as e:
#     print("Ошибка ввода: введите два числа через пробел")
#     print(f"Текст ошибки: {e}")
# except ZeroDivisionError as e:
#     print("На ноль делить нельзя!")
#     print(f"Текст ошибки: {e}")
# except Exception as e:
#     print("Произошла неизвестная ошибка")
# else:
#     print(res)
#
# """11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
# Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку."""
# class Calc:
#     def calculator(self, operation, a: float, b: float):
#         try:
#             if operation == "+":
#                 return a + b
#             elif operation == "-":
#                 return a - b
#             elif operation == "*":
#                 return a * b
#             elif operation == "/":
#                 return a / b
#             elif operation == "**":
#                 return a ** b
#             else:
#                 raise ValueError("Неизвестная операция")
#
#         except ValueError as er:
#             print(f"Ошибка: {er}")
#
#         except ArithmeticError as er:
#             print(f"Арифметическая ошибка: {er}")
#
#
# test = Calc()
# print(test.calculator("*",4,5))
# print(test.calculator('/', 10, 0))
#
#
# """12. Запроси у пользователя два числа и выполни деление.
# Если деление прошло успешно без ошибок — выведи
# "Деление выполнено успешно" через (но не в блоке try)"""
# """13. Расширь код из Задания 12:
# Добавь блок, в котором будет выводиться
# "Работа программы завершена", независимо от успеха деления."""
#
#
# positive = ""
# try:
#     num_1 = input("Введите первое число: ")
#     num_2 = input("Введите второе число: ")
#     num_1, num_2 = float(num_1), float(num_2)
#     res = num_1 / num_2
#     positive = "Деление выполнено успешно"
# except Exception as e:
#     pass
# finally:
#     print("Работа программы завершена")
# if positive == "Деление выполнено успешно":
#     print(positive)

"""14. Реализуй две вложенные конструкции:
Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
Внутренний try/except ловит деление на ноль."""

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    try:
        result = num1 / num2
        print(f"Результат деления: {result}")
    except ZeroDivisionError as e:
        print(f"Ошибка деления: {e}")
except ValueError as e:
    print(f"Ошибка ввода: {e}")



"""15. Вынеси обработку деления в отдельную функцию divide(x, y)
с собственным try/except.
Во внешнем коде обработай только ошибку ввода."""


def divide(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError as e:
        print(f"Ошибка деления: {e}")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = divide(num1, num2)
    if result is not None:
        print(f"Результат деления: {result}")
    else:
        print("Деление не выполнено из-за ошибки")
except ValueError as e:
    print(f"Ошибка ввода: {e}")