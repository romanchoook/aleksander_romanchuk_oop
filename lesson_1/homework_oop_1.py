# ++++++++++++++++++++++++++++++++++++++
# Классы и атрибуты
# ++++++++++++++++++++++++++++++++++++++
# ======================================
# 1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
# Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
# Проверь, как это повлияло на значения у обоих объектов.
# Убедись, что __dict__ объектов отражает изменения.
class Dog:
    "Класс Dog содержит аттрибуты: количество лап  (legs) и вид (species)"
    species = "canis"
    legs = 4

dog_1 = Dog()
dog_2 = Dog()

dog_1.legs = 3
print(f"Dog legs = {Dog.legs}")
print(f"dog_1 legs = {dog_1.legs}")
print(f"dict Dog - {Dog.__dict__}")
print(f"dict dog_1 - {dog_1.__dict__}")
print(f"dict dog_2 - {dog_2.__dict__} - изменений нет")

# 2. Добавь в класс Dog строку документации, описывающую его назначение.
# Затем выведи её на экран.
# После этого добавь в объект класса новые атрибуты name и age,
# а затем удали name.
# Проверь, что произойдёт при попытке снова вывести объект.name.
print(Dog.__doc__)
dog_2.name = 0
dog_2.age = 0

del dog_2.name
#print(dog_2.name) #- в консоли ошибка AttributeError: 'Dog' object has no attribute 'name'"
# 3. Создай класс User с атрибутами класса role = "guest" и active = True.
# С помощью функций getattr(), setattr(), hasattr() и delattr():
#
# измени значение role на "admin",
# проверь наличие active,
# добавь новый атрибут email,
# удали role.
# Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.

class User:
    role = "guest"
    active = True

setattr(User, "role", "admin")
print(User.role)
print(hasattr(User, "active"))
setattr(User, "email", 0)
delattr(User, "role")
print(User.__dict__)