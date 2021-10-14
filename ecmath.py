class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y


class EllipticCurve:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set_a(self, a):
        self.a = a

    def get_a(self):
        return self.a

    def set_b(self, b):
        self.b = b

    def get_b(self):
        return self.b

    def isNonSingular(self):
        return (4*(self.a**3)+27*(self.b**2)) != 0

    def belongsToCurve(self, point):
        return (point.get_y**2) == ((point.get_x**3)+self.a*self.x+self.b)

    def point_addition(self, point_p, point_q):
        alpha = (point_q.get_y() - point_p.get_y())/(point_q.get_x() - point_p.get_x())

        point_r = Point()
        point_r.set_x(alpha**2 - point_p.get_x() - point_q.get_x())
        point_r.set_y(alpha*(point_r.get_x() - point_p.get_x()) + point_p.get_y())

        point_pq = Point()
        point_pq.set_x(alpha**2 - point_p.get_x() - point_q.get_x())
        point_pq.set_y(alpha*(point_p.get_x() - point_r.get_x()) - point_p.get_y())

        return point_pq