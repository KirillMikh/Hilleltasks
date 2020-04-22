import pytest
from random import randint


class Rectangle():
    def __init__(self, list1: list):
        if len(list1) != 2:
            raise TypeError("не 2 стороны")
        if list1[0] <= 0 or list1[1] <= 0:
            raise AttributeError("Сторона не может быть отрицательной или нулевой")

        self.a = list1[0]
        self.b = list1[1]

    def P(self):
        return self.a * 2 + self.b * 2

    def S(self):
        return self.a * self.b


def test_P():
    side1 = randint(0,200)
    side2 = randint(0, 200)
    r1 = Rectangle([side1, side2])
    assert side1*2+side2*2 == r1.P()


def test_rectangle_negative_and_zero_arguments():
    with pytest.raises(AttributeError):
        Rectangle([-2, 1])

    with pytest.raises(AttributeError):
        Rectangle([0, 0])

    with pytest.raises(AttributeError):
        Rectangle([-5, -5])


def test_rectangle_list_arguments():
    with pytest.raises(TypeError):
        Rectangle([4, 5, 6, 7, 8])

    with pytest.raises(TypeError):
        Rectangle([])


def test_S():
    side1 = randint(0, 1000)
    side2 = randint(0, 1000)
    r1 = Rectangle([side1, side2])
    assert side1*side2 == r1.S()










