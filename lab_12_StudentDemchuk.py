import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def gety(self):
        return self._y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__allVertice = [vertice1, vertice2, vertice3]

    def perimeter(self):
        distancesA_B = math.hypot(self.__allVertice[0].getx() - self.__allVertice[1].getx(),
                                  self.__allVertice[0].gety() - self.__allVertice[1].gety())
        distancesB_C = math.hypot(self.__allVertice[1].getx() - self.__allVertice[2].getx(),
                                  self.__allVertice[1].gety() - self.__allVertice[2].gety())
        distancesC_A = math.hypot(self.__allVertice[2].getx() - self.__allVertice[0].getx(),
                                  self.__allVertice[2].gety() - self.__allVertice[0].gety())

        perimeter = distancesA_B + distancesB_C + distancesC_A
        return perimeter


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
