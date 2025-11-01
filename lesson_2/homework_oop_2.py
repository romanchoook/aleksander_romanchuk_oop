"""1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
Создай два объекта и задай им разные значения. Выведи информацию по каждому."""
class Person:
    def set_data(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

person = Person()
person_2 = Person()
person.set_data("Александр", 30)
person_2.set_data("Даниил", 35)
print(person.get_data())
print(person_2.get_data())

"""2. Добавь в класс Point методы set_coords(x, y) и get_coords().
Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
После этого измени координаты на (-3, 5) и снова выведи результат через get_coords()."""
class Point:
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

p = Point()
p.set_coords(7, 12)
res = p.get_coords()
print(res)
p.set_coords(-3, 5)
print(p.get_coords())

"""3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
Проверь, что результат совпадает с обычным вызовом p.get_coords()."""
res_1 = getattr(Point, 'get_coords')
res_2 = res_1(p)
print(res_2)
print(f"Результаты совпадают: {res_2 == p.get_coords()}")


""""4. Создай класс Person, в котором метод __init__() принимает имя и возраст и сохраняет их как атрибуты объекта.
Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод."""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"Имя: {self.name}, возраст: {self.age}"

    def __del__(self):
        print(f"Удален объект: {self.name}")

person = Person("Александр", 30)
print(person.show_info())


"""5. Добавь в класс Person метод __del__(), который выводит сообщение "Удалён объект: <имя>",
где <имя> — значение поля name. Создай и удали объект вручную с помощью del."""
person_2 = Person("Даниил", 35)
del person_2

"""6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
Добавь метод area(), который возвращает площадь прямоугольника.
Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой."""
class Rectangle:
    def __init__(self, width: int = 1, height: int = 1):
        self.width = width
        self.height = height

    def area(self):
        return f"Площаль прямоугольника: {self.width * self.height}"

rectangle = Rectangle()
print(rectangle.area())
rectangle_1 = Rectangle(4,5)
print(rectangle_1.area())

"""7. Создай класс Logger, который всегда возвращает один и тот же объект.
При создании экземпляра в __new__ выводи Создание логгера,
а при вызове __init__ — Инициализация логгера."""
class Logger:
    instance = None

    def __new__(cls, *args, **kwargs):
        print("Создание логгера")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("Инициализация логгера")

obj = Logger()
