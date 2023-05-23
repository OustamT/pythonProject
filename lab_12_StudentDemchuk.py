import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__allVertice = [vertice1, vertice2, vertice3]

    def perimeter(self):
        #
        # __allVertice[0]
        #


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())