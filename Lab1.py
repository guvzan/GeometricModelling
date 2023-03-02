from graphics import *
from math import sqrt
from random import randint

class HexPattern:
    """
    Побудова узора на основі шестикутників
    """
    def __init__(self):
        #Використати випадкові значення?
        self._GO_RANDOM = False
        if self._GO_RANDOM:
            self._random_set()
        else:
            self._manual_set()

        #Розміри вікна
        self.WIDTH = 500
        self.HEIGHT = 500

        #Інші налаштування (не змінювати)
        self._X_RANDOM = randint(0, 100)
        self._Y_RANDOM = randint(0, 100)
        self._X_BTW_POINTS = self.MAX_HEX_RADIUS * sqrt(3)

    def _manual_set(self):
        """Ручне задання параметрів"""
        self.MAX_HEX_RADIUS = 170   # Максимальний радіус шестикутника
        self.LINE_WIDTH = 2         # Товщина ліній
        self.RATIO = 10             # Відстань між шестикутниками однієї точки

    def _random_set(self):
        """Випадкові значення"""
        self.MAX_HEX_RADIUS = randint(50, 200)
        self.LINE_WIDTH = randint(1, 3)
        self.RATIO = randint(5, 10)

    def _form_points(self):
        """
        Сформувати точки, навколо яких
        необхідно виконувати побудову
        шестикутників
        """
        x_num = self.WIDTH / self._X_BTW_POINTS
        y_num = self.HEIGHT / self.MAX_HEX_RADIUS

        # Головна діагональ
        points = [Point(i * (self._X_BTW_POINTS + self.RATIO) - self._X_RANDOM,
                        i * (self.MAX_HEX_RADIUS + self.RATIO) - self._Y_RANDOM) for i in range(int(x_num + 2))]
        main_points_len = len(points)

        # Розширення
        for i in range(main_points_len):
            x = points[i].getX()
            y = points[i].getY()
            # Вниз
            for j in range(int(y_num) - i + 2):
                points.append(Point(x, y + j * (self.MAX_HEX_RADIUS * 2 + self.RATIO)))
            # Вверх
            for j in range(i + 1):
                points.append(Point(x, y - j * (self.MAX_HEX_RADIUS * 2 + self.RATIO)))
        return points

    def get_hexagon(self, point, r):
        """
        Отримати шестикутник заданого радіусу
        навколо заданої точки
        """
        a = 2 * r / sqrt(3)
        x = point.getX()
        y = point.getY()
        points = [Point(x - a, y), Point(x - (a / 2), y + r), Point(x + (a / 2), y + r), Point(x + a, y),
                  Point(x + (a / 2), y - r), Point(x - (a / 2), y - r)]
        hex = Polygon(points)
        hex.setWidth(self.LINE_WIDTH)
        return hex

    def build_pattern(self):
        """Виконати побудову узора"""
        self.win = GraphWin('Test', self.WIDTH, self.HEIGHT, autoflush=False)
        self.points = self._form_points()
        for point in self.points:
            for i in range(1, self.MAX_HEX_RADIUS + self.RATIO, int(self.RATIO)):
                self.get_hexagon(point, i).draw(self.win)
        self.win.getMouse()
        self.win.close()


if __name__ == '__main__':
    builder = HexPattern()
    builder.build_pattern()