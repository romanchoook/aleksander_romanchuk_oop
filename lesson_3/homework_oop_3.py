import math
pi = math.pi
"""======================================
1. Создай класс Circle, в котором:
есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
Проверь результат вызова:
print(Circle.is_valid_radius(500))   # True
print(Circle.is_valid_radius(1500))  # False
======================================"""
class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    def __init__(self, radius):
        assert self.is_valid_radius(radius), f"Радиус {radius} должен быть между {self.MIN_RADIUS} и {self.MAX_RADIUS}"
        self.radius = radius

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return pi * (radius ** 2)

    def print_info(self):
        print(f"Радиус: {self.radius}")
        print(f"Допустимый диапазон: [{type(self).MIN_RADIUS}, {type(self).MAX_RADIUS}]")



print(Circle.is_valid_radius(500))
print(Circle.is_valid_radius(1500))


"""2. Добавь в класс Circle:
статический метод area(radius),
который возвращает площадь круга по формуле π * r ** 2 (используй импорт math.pi),
инициализацию в __init__, которая сохраняет радиус,
только если он проходит валидацию через метод is_valid_radius()
(подумай как можно проверить значения перед тем как записать их в переменные экземпляра класса)
Пример:
c = Circle(10)
print(c.area(c.radius))  # Площадь круга
======================================"""
c = Circle(10)
print(c.area(c.radius))


"""3. Расширь Circle, добавив обычный метод print_info, который выводит:
Радиус: ...
Допустимый диапазон: [MIN, MAX]
Метод должен использовать и self, и атрибуты класса через type(self).

Пример вызова:
c.print_info()
======================================"""
c.print_info()

"""4. Создай класс User, в котором:

приватные атрибуты __login и __password;
метод set_credentials(login, password), который сохраняет их только если оба значения — строки;
метод get_credentials(), который возвращает кортеж из логина и пароля.
Попробуй создать объект и изменить логин снаружи напрямую. Проверь, что это не сработает.
======================================"""
class User:
    def __init__(self):
        self.__login = ""
        self.__password = ""

    def set_credentials(self, login: str, password: str):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = password
            return "Логин и пароль сохранены"
        else:
            return "Логин или пароль не являются строковыми"

    def  get_credentials(self):
        return (self.__login, self.__password)

    """5. Добавь в User:
    метод check_password(password) — возвращает True,
    если переданное значение совпадает с сохранённым паролем;
    приватный метод __encrypt_password(password),
    который возвращает пароль в верхнем регистре (имитация шифрования);
    в set_credentials вызывай __encrypt_password.
    Пример:
    u = User()
    u.set_credentials("daniil", "qwerty")
    print(u.check_password("qwerty"))      # True
    print(u.check_password("qwe"))         # False
    ======================================"""
    def check_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

    def __encrypt_password(self, password):
        return password.upper()


try1 = User()
print(try1.set_credentials("admin", "paass123"))
print(try1.get_credentials())
try1.__login = "user"
try1.__password = "pass"
print(try1.get_credentials()) # - доступ к приватным аттрибутам только внутри класса, снаружи их изменить не получится, внутри метода останутся значения метода set
u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty"))
print(u.check_password("qwe"))
print(u.get_credentials())
"""6. Убедись, что приватный метод __encrypt_password нельзя вызвать извне.
Попробуй это сделать — и поясни результат.
Также выведи напрямую u.__password — и проверь, что будет ошибка.

Попробуй добраться до данных через u._User__password"""
# result = u.__encrypt_password("test")
# print(result) """- ошибка AttributeError: 'User' object has no attribute '__encrypt_password' - чтобы обратиться к protect аттрибуту или методу
# нужно обращаться через класс с "_", а не с объектом"""
print(u._User__password)