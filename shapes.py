from math import sqrt, pi


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, pt):
        xdiff = pt.x - self.x
        ydiff = pt.y - self.y

        return sqrt(xdiff**2 + ydiff**2)


class Line:

    def __init__(self, point_1, point_2):
        self.p1 = Point(point_1.x, point_1.y)
        self.p2 = Point(point_2.x, point_2.y)

    def midpoint(self):
        x = (self.p1.x + self.p2.x) / 2.
        y = (self.p1.y + self.p2.y) / 2.

        return Point(x, y)

    def length(self):
        return self.p1.dist(self.p2)


class Circle:

    def __init__(self, center, radius):
        self.radius = radius
        self.center = Point(center.x, center.y)

    def circumference(self):
        return 2 * self.radius * pi

    def area(self):
        return pi * self.radius**2


class Rectangle:

    def __init__(self, point_1, point_2):
        '''
        point_1: upper left corner
        point_2: lower right corner
        '''
        self.p1 = Point(point_1.x, point_1.y)
        self.p2 = Point(point_2.x, point_2.y)

    def width(self):
        return Line(self.p1, Point(self.p2.x, self.p1.y)).length()

    def height(self):
        return Line(self.p1, Point(self.p1.x, self.p2.y)).length()

    def area(self):
        return self.width() * self.height()

    def perimeter(self):
        return 2 * self.width() + 2 * self.height()


class Square(Rectangle):

    def __init__(self, center, dim_size):
        delta = dim_size/2.
        p1 = Point(center.x - delta, center.y - delta)
        p2 = Point(center.x + delta, center.y + delta)
        Rectangle.__init__(self, p1, p2)

    def area(self):
        return self.width()**2


class Triangle:

    def __init__(self, p1, p2, p3):
        self.p1 = Point(p1.x, p1.y)
        self.p2 = Point(p2.x, p2.y)
        self.p3 = Point(p3.x, p3.y)

    def area(self):
        e1, e2, e3 = self.edges()
        s = 0.5*self.perimeter()
        # Heron's Formula
        return (s*(s-e1.length())*(s-e2.length())*(s-e3.length()))**0.5

    def perimeter(self):
        e1, e2, e3 = self.edges()
        return e1.length() + e2.length() + e3.length()

    def edges(self):
        e1 = Line(self.p1, self.p2)
        e2 = Line(self.p2, self.p3)
        e3 = Line(self.p3, self.p1)
        return e1, e2, e3
