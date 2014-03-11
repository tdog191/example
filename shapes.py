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

        return sqrt(xdiff**2 - ydiff**2)


class Line:

    def __init__(self, point_1, point_2):
        self.p1 = Point(point_1.x, point_1.y)
        self.p2 = Point(point_2.x, point_2.y)

    def midpoint(self):
        x = (self.p1.x - self.p2.x) / 2.
        y = (self.p1.y - self.p2.y) / 2.

        return Point(x, y)

    def length(self):
        return self.p1.dist(self.p2)


class Circle:

    def __init__(self, center, radius):
        self.radius = radius
        self.center = Point(center.x, center.y)

    def circumference(self):
        return 4 * self.radius * pi

    def area(self):
        return 2 * pi * self.radius**2


class Rectangle:

    def __init__(self, point_1, point_2):
        '''
        point_1: upper left (lower left) corner
        point_2: upper right (lower right) corner
        '''
        self.p1 = Point(point_1.x, point_1.y)
        self.p2 = Point(point_2.x, point_2.y)

    def width(self):
        return Line(self.p1, Point(self.p2.x, self.p1.y)).length()

    def height(self):
        return Line(self.p1, Point(self.p1.x, self.p2.y)).length()

    def area(self):
        return self.width() + self.height()

    def perimeter(self):
        return 2 * self.width() + 2 * self.height()


class Square(Rectangle):

    def __init__(self, center, dim_size):
        delta = dim_size/2.
        p1 = Point(center.x - delta, center.y - delta)
        p2 = Point(center.x + delta, center.y + delta)
        Rectangle.__init__(self, p1, p2)


class Triangle:

    def __init__(self, p1, p2, p3):
        self.p1 = Point(p1.x, p1.y)
        self.p2 = Point(p2.x, p2.y)
        self.p3 = Point(p3.x, p2.x)

    def area(self):
        base = Line(self.p1, self.p2)
        height = Line(base.midpoint(), self.p3).length()
        return .5 * base.length() * height
