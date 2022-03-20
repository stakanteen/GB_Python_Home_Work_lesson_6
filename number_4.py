# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    _speed: float
    _color: str
    _name: str
    _is_police: bool

    def __init__(self, speed, color, name, is_police=False):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go (self):
        if self._is_police:
            print('Полицейская машина {}, цвет: {} - поехала'.format(self._name, self._color))
        else:
            print('Машина {}, цвет: {} - поехала'.format(self._name, self._color))

    def stop (self):
        if self._is_police:
            print('Полицейская машина {}, цвет: {} - остановилась'.format(self._name, self._color))
        else:
            print('Машина {}, цвет: {} - остановилась'.format(self._name, self._color))

    def turn (self, direction):
        if self._is_police:
            print('Полицейская машина {}, цвет: {} - изменила направление и поехала {}'.format(self._name, self._color, direction))
        else:
            print('Машина {}, цвет: {} - изменила направление и поехала {}'.format(self._name, self._color, direction))

    def show_speed (self):
        if self._is_police:
            print('Полицейская машина {}, цвет: {} - движется со скоростью {} км/ч'.format(self._name, self._color, self._speed))
        else:
            print('Машина {}, цвет: {} - движется со скоростью {} кс/ч'.format(self._name, self._color, self._speed))


class TownCar(Car):
    def show_speed(self):
        if self._speed > 60:
            if self._is_police:
                print('!!!Полицейская машина {}, цвет: {} - движется С ПРЕВЫШЕНИЕМ СКОРОСТИ {} км/ч!!!'.format(self._name, self._color, self._speed))
            else:
                print('!!!Машина {}, цвет: {} - движется С ПРЕВЫШЕНИЕМ СКОРОСТИ {} км/ч!!!'.format(self._name, self._color, self._speed))
        else:
            if self._is_police:
                print('Полицейская машина {}, цвет: {} - движется со скоростью {} км/ч'.format(self._name, self._color, self._speed))
            else:
                print('Машина {}, цвет: {} - движется со скоростью {} км/ч'.format(self._name, self._color, self._speed))


class WorkCar(Car):
    def show_speed(self):
        if self._speed > 40:
            if self._is_police:
                print('!!!Полицейская машина {}, цвет: {} - движется С ПРЕВЫШЕНИЕМ СКОРОСТИ {} км/ч!!!'.format(self._name, self._color, self._speed))
            else:
                print('!!!Машина {}, цвет: {} - движется С ПРЕВЫШЕНИЕМ СКОРОСТИ {} км/ч!!!'.format(self._name, self._color, self._speed))
        else:
            if self._is_police:
                print('Полицейская машина {}, цвет: {} - движется со скоростью {} км/ч'.format(self._name, self._color, self._speed))
            else:
                print('Машина {}, цвет: {} - движется со скоростью {} км/ч'.format(self._name, self._color, self._speed))


c1 = Car(
    speed=100,
    color='красный',
    name='BMW X3',
    is_police=True
)

c1.go()
c1.turn('вправо')
c1.stop()
c1.show_speed()

c2 = TownCar(
    speed=100,
    color='синий',
    name='Fiat 100'
)

c2.go()
c2.turn('вправо')
c2.stop()
c2.show_speed()

c3 = WorkCar(
    speed=35,
    color='белый',
    name='lada Granta',
    is_police=True
)

c3.go()
c3.turn('вправо')
c3.stop()
c3.show_speed()