# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# Важно!
# При отправке домашнего задания обязательно нажимайте галочку "Показать задание ментору".

class Stationery:
    _title: str

    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Запуск отрисовки чего-то с названием {}'.format(self._title))

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручки с названием {}'.format(self._title))

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандаша с названием {}'.format(self._title))

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркера с названием {}'.format(self._title))

smth = Stationery(title='something')
smth.draw()

pen = Pen(title='Black Pen')
pen.draw()

pencil = Pencil(title='Red Pencil')
pencil.draw()

handle = Handle(title='Rose Handle')
handle.draw()