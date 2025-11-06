"""1. Создай класс SecureData, который:

имеет атрибут __secret, задаваемый в __init__;
переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
внутри класса доступ к __secret должен работать.
Проверь:
data = SecureData("пароль123")
print(data.__secret)      # ошибка
print(data.get_secret())  # "пароль123"""
from datetime import datetime


class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, item):
        if item == '_SecureData__secret':
            raise ValueError("Попытка получить __secret извне")
        return object.__getattribute__(self, item)

    def get_secret(self):
        return object.__getattribute__(self, '_SecureData__secret')

    def __setattr__(self, key, value):
        if key == "token":
            raise ValueError(f"Аттрибут не может называться 'token'")
        object.__setattr__(self, key, value)

data = SecureData("пароль123")
# print(data.__secret)
print(data.get_secret())
# data.token = "abc123"
data.other = "ok"
"""2. Добавь в класс SecureData метод __setattr__,
который запрещает создание любого атрибута с именем token.

Проверь:
data.token = "abc123"  # ❌ AttributeError
data.other = "ok"      # ✅ работает"""

"""3. Создай класс SafeDict, в котором:

нет атрибута default;
реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
Проверь:
d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"""

class SafeDict:
    def __getattr__(self, name):
        print("N/A")
        return None

    def __delattr__(self, name):
        print(f"Удален атрибут {name}")
        object.__delattr__(self, name)
d = SafeDict()
print(d.unknown)
d.key = 10
del d.key

"""4. Создай класс Employee с приватными полями __name и __salary.
Добавь @property для поля salary, а также сеттер с валидацией:

зарплата должна быть положительным числом;
если нет — выбрасывать ValueError.
Проверь, что:
e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
e.salary = -100   # ❌ ValueError"""

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError("Зарплата должна быть положительным числом")
        self.__salary = value

    @salary.deleter
    def salary(self):
        print("Зарплата удалена")
        object.__delattr__(self, '_Employee__salary')




e = Employee("Daniil", 5000)
print(e.salary)
e.salary = 8000
print(e.salary)
# e.salary = -100

"""5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
и поле реально исчезало.
Проверь:

del e.salary
print(e.__dict__)  # salary нет"""
del e.salary
print(e.__dict__)

"""6. Представь, что ты пишешь обёртку над HTML-формой.
Создай класс LoginForm с полем username, которое реализовано через @property.

Логика:
геттер возвращает self._username
сеттер добавляет лог "username изменён"
Проверь, что:
form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # "admin"""

class LoginForm:

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        print("username изменен")
        self._username = value


form = LoginForm()
form.username = "admin"
print(form.username)
"""7. Создай класс Card, где:
поле __number хранит номер карты (строка);
в @property возвращай номер с маской **** **** **** 1234;
в @setter проверяй, что номер состоит из 16 цифр;
в @deleter логируй удаление номера с текущим временем.
Напиши тесты (через assert)
проверку установки корректного номера;
проверку исключения при вводе короткого номера;
проверку вывода замаскированного номера."""
class Card:
    def __init__(self, number: str):
        self.__number = number

    @property
    def number(self):
        return "**** **** **** " + self.__number[-4:]

    @number.setter
    def number(self, value):
        assert value.isdigit(), 'Номер карты должен содержать только цифры'
        assert len(value) == 16, 'Номер карты должен содержать 16 цифр'
        self.__number = value

    @number.deleter
    def number(self):
        print(f"[LOG] "
              f"{datetime.now().strftime("%Y.%m.%d %H:%M:%S")} "
              f"Карта удалена")
        object.__delattr__(self, '_Card__number')

card = Card("1234567890123456")
assert card._Card__number == "1234567890123456", "Установлен некорректный номер"
# card.number = "1234" """AssertionError: Номер карты должен содержать 16 цифр"""
# card.number = "12341234123412341234" """AssertionError: Номер карты должен содержать 16 цифр"""
# card.number = "1234asdf32111234"  """AssertionError: Номер карты должен содержать только цифры"""
# assert card.number == "1234", "Номер карты должен содержать 16 цифр"
# assert card.number == "12341234123412341234", "Номер карты должен содержать 16 цифр"
masked = card.number
assert masked == "**** **** **** 3456", "Номер маскируется неверно"
del card.number

"""8. Создай класс UserData для API регистрации пользователя:
email — строка, содержит @;
age — целое число ≥ 18;
is_active — bool;
свойство .json возвращает словарь для запроса.
Напиши тест (через assert)
проверь, что при age = 15 выбрасывается ValueError;
проверь, что email без @ вызывает ошибку;
проверь, что json возвращает корректную структуру."""

class UserData:
    def __init__(
            self,
            email: str,
            age: int,
            is_active: bool,
            ):
        self.__email = email
        self.__age = age
        self.__is_active = is_active

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email должен быть строкой")
        if "@" not in value:
            raise ValueError("Email должен содержать символ @")
        self.__email = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Возраст должен быть целым числом")
        if value < 18:
            raise ValueError("Возраст должен быть >= 18")
        self.__age = value

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value):
        if not isinstance(value, bool):
            raise ValueError('Значение может быть только булевым значением')
        self.__is_active = value

    @property
    def json(self):
        return {
            "email": self.email,
            "age": self.age,
            "is_active": self.is_active,
        }

userdata = UserData("email@email", 30, True)

# assert userdata.age == 15, "value error"
# assert userdata.email == "emailemail", 'email без собаки'
assert userdata.json["is_active"] is True
print(userdata.json)