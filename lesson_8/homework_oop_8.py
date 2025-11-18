import math
import time
"""1. Создай две функции: inner() и outer().
В inner() вызови деление на ноль.
В outer() просто вызови inner().
Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов."""
def inner():
    result = 1/0
    return result

def outer():
    result = inner()
    return result

# outer() - Traceback (most recent call last):
#   File "C:\Users\Александр\PycharmProjects\aleksander_romanchuk_oop\lesson_8\homework_oop_8.py", line 15, in <module>
#     outer()
#     ~~~~~^^
#   File "C:\Users\Александр\PycharmProjects\aleksander_romanchuk_oop\lesson_8\homework_oop_8.py", line 12, in outer
#     result = inner()
#   File "C:\Users\Александр\PycharmProjects\aleksander_romanchuk_oop\lesson_8\homework_oop_8.py", line 8, in inner
#     result = 1/0
#              ~^~
# ZeroDivisionError: division by zero


"""2. Добавь вокруг вызова outer() конструкцию try/except,
чтобы перехватить исключение и вывести сообщение
"Ошибка перехвачена на верхнем уровне"."""
try:
    outer()
except ZeroDivisionError as e:
    print("Ошибка перехвачена на верхнем уровне")

"""3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
В случае ошибки возвращай строку "Ошибка в inner"."""
def inner_2():
    try:
        result = 1/0
    except ZeroDivisionError as e:
        return "Ошибка в inner"
    else:
        return result

def outer_2():
    result = inner_2()
    return result
outer_2()
"""4. Сделай так:
В inner() ошибка не перехватывается.
В outer() ошибка перехватывается через try/except.
В outer() при перехвате напечатай "Ошибка в outer"."""
def inner_3():
    result = 1 / 0
    return result

def outer_3():
    try:
        result = inner_3()
    except ZeroDivisionError as e:
        print("Ошибка в outer")
    else:
        return result
outer_3()
"""5. Напиши функцию get_value(), которая кидает ValueError.
Напиши тестовую функцию test_get_value(), которая:

Вызывает get_value();
Ловит ValueError;
Завершает тест с assert False, если исключение поймано."""
def get_value():
    raise ValueError

def test_get_value():
    try:
        get_value()
        assert False
    except ValueError as e:
        pass

test_get_value()



"""6. Создай функцию divide(x, y).
Если y == 0, выбрасывай ZeroDivisionError через raise.
Иначе возвращай результат деления."""
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль")
    else:
        return x / y



"""7. Создай функцию sqrt(x), которая:
Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
Иначе возвращает квадратный корень из x.
Проверь поведение функции через try/except."""
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Число {self.value} не может быть отрицательным"

def sqrt(x):
    if x < 0:
        raise NegativeNumberError(x)
    else:
        return math.sqrt(x)

try:
    sqrt(-5)
except NegativeNumberError as e:
    print("Тест с отрицательным числом (-5) пройден")

try:
    sqrt(36)
except NegativeNumberError as e:
    print("Тест с положительным числом (36) не пройден")
else:
    print(sqrt(36))



"""8. Создай базовый класс MathError.
От него унаследуй:
NegativeNumberError
DivisionByZeroError
В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
Проверь в try/except обработку ошибок через базовый класс MathError."""
class MathError(Exception):
    pass

class NegativeNumberError(MathError):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Число {value} не может быть отрицательным")

class DivisionByZeroError(MathError):
    def __init__(self):
        super().__init__("Деление на ноль невозможно")

def safe_divide(x,y):
    if y == 0:
        raise DivisionByZeroError()
    else:
        return x / y

try:
    safe_divide(4, 0)
except MathError as e:
    print("Словили деление на ноль")


"""9. Создай тестовую функцию test_sqrt(), которая:
вызывает sqrt(x) с отрицательным числом;
перехватывает NegativeNumberError;
завершает тест с assert False и сообщением
"Нельзя брать корень из отрицательного числа"."""

def test_sqrt():
    try:
        sqrt(-5)
        assert False, "Нельзя брать корень из отрицательного числа"
    except NegativeNumberError as e:
        print("NegativeNumberError перехвачен")

test_sqrt()


"""10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
Обеспечь закрытие файла через with."""
with open("sample.txt") as f:
    for line in f:
        print(line, end="")


"""11. Создай класс BackupList, который:
делает копию списка при входе в with,
при выходе сохраняет изменения, если ошибок не было,
откатывает изменения при ошибке.
Проверь:
успешное изменение списка;
откат при ошибке."""
class BackupList:
    def __init__(self, original_list):
        self.original_list = original_list
        self.backup = None
        self.new_list = None

    def __enter__(self):
        self.backup = self.original_list.copy()
        self.new_list = self.original_list
        return self.new_list

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"Итоговый список: {self.original_list}")
        else:
            print("Откатываем изменения к резервной копии")
            self.original_list[:] = self.backup
            print(f"Восстановленный список: {self.original_list}")

        self.backup = None
        self.new_list = None
        return False


numbers = [1, 2, 3]
print(f"Исходный список: {numbers}")
try:
    with BackupList(numbers) as lst:
        lst.append(4)
        lst.append(5)
        result = 10 / 0  # Вызовет ZeroDivisionError

except ZeroDivisionError:
    print("Поймано ZeroDivisionError")

print(f"Список после деления на ноль: {numbers}")
print()

numbers_1 = [1, 2, 3]
print(f"До: {numbers_1}")

with BackupList(numbers_1) as lst:
    lst.append(4)
    lst[0] = 100

print(f"После: {numbers_1}")
print()


"""12. Создай декоратор-класс Timer,
который измеряет время выполнения функции и выводит результат."""

class Timer:
    def __init__(self, func):
        self.func = func


    def measure_time(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        res = end - start
        print(f"Код выполнялся {res} сек")
        return result

    def __call__(self, *args, **kwargs):
        return self.measure_time(*args, **kwargs)

@Timer
def test_timer():
    print("Тест таймера:")

test_timer()