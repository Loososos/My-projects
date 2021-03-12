
from sympy import *
from scipy.misc import derivative

print('Программа работает с функцией материальной точки вида: x0 + v0 * t + (a * t ** 2)/2 ')
v0=int(input('Введите начальную скорость: '))
x0=int(input('Введите начальную точку (координату x): '))
a=int(input('Введите ускорение: '))


class Speed:
    '''Класс для определения скорости, ускорения и количество пройденного пути матреиальной точкой'''
    def __init__(self):
        self.t = float(input('Введите время пройденное точкой: '))
        self.r = 0

    @staticmethod
    def difer(x,t):
        '''Метод для определения функции движения материальной точки'''
        print(Speed.r)
        return  x0 + v0 * t + (a * t ** 2)/2

    def show(self):
        '''Метод для вывода функции движения материальной точки'''
        t = symbols('t')
        print('\nФункция движения точки: ')
        return  x0 + v0 * t + (a * t ** 2)/2

    def speed(self):
        '''Метод для определения скорости материльной точки в определенный время'''
        x = symbols('t')
        print('\nФункция для расчета скорости движения материальной точки(первая производная): ')
        print( diff(x0 + v0 * x + (a * x ** 2)/2, x))
        print('\nСкорость материальной точки через ',self.t,' секунд(m/c): ')
        return derivative(x0 + v0 * t + (a * t ** 2)/2, self.t, dx=0.1, n=1)


    def impuls(self):
        '''Метод для определения ускорения материальной точки в определеное время'''
        x = symbols('x')
        print('\nФункция для расчета ускорения движения материальной точки(вторая производная): ')
        print(diff(v0 + a*x, x))
        print('\nУскорение материальной точки через ', self.t, ' секунд(m/с^2): ')
        return derivative(Speed.difer, self.t, dx=0.1,n=2)


    def where(self):
        '''Метод для определения количество пройденного пути материльной точки за определенное время'''
        print('\nРастояние пройденное точкой(метры):')
        return x0 + v0 * self.t + (a * self.t ** 2)/2

c=Speed()
print(c.show())
print(c.speed())
print(c.impuls())
print(c.where())
