from math import *
class Object:
  def a(self):
    return self.b()

  def b(self):
    return 'A'

class Y(Object):
  def b(self):
    return 'B'

class Circle:
  def __init__(self, radius):
    self.radius = radius
  def calcArea(self):
    return pi *self.radius**2

class Square:
  def __init__(self, side):
    self.side = side
  def calcArea(self):
    return self.side ** 2

L = [Circle(3), Square(5), Circle(333), Square(99), Square(32), Circle(23), Circle(21),Square(24)]
for shape in L:
  print("the area of the shape is:", shape.calcArea())