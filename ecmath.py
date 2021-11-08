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

    def print(self):
        return "("+str(round(self.x, 5))+", "+str(round(self.y, 5))+")"


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
        return (point.get_y()**2) == ((point.get_x()**3)+self.a*point.get_x()+self.b)

    def point_addition(self, point_p, point_q):
        alpha = (point_q.get_y() - point_p.get_y())/(point_q.get_x() - point_p.get_x())

        point_r = Point()
        point_r.set_x(alpha**2 - point_p.get_x() - point_q.get_x())
        point_r.set_y(alpha*(point_r.get_x() - point_p.get_x()) + point_p.get_y())

        point_pq = Point()
        point_pq.set_x(alpha**2 - point_p.get_x() - point_q.get_x())
        point_pq.set_y(alpha*(point_p.get_x() - point_r.get_x()) - point_p.get_y())

        return point_pq

    def point_doubling(self, point):
        alpha = (3 * point.get_x() ** 2 + self.get_a()) / (2 * point.get_y())

        point_r = Point()
        point_r.set_x(alpha ** 2 - 2 * point.get_x())
        point_r.set_y(alpha*(point.get_x() - point_r.get_x()) - point.get_y())

        return point_r

    def point_mult(self, point, k):
        point_r = self.point_doubling(point)
        for x in range(k-2):
            point_r = self.point_addition(point, point_r)

        return point_r

    def print(self):
        text = "y\u00B2 = x\u00B3"
        if self.a > 0:
            text += (" + " + str(self.a) + "x")
        elif self.a < 0:
            text += (" " + str(self.a) + "x")

        if self.b > 0:
            text += (" + " + str(self.b))
        elif self.b < 0:
            text += (" "+str(self.b))

        return text


class User:
    def __init__(self):
        self.privKey = 0
        self.pubKey = 0

    def setPrivKey(self, privKey):
        self.privKey = privKey

    def getPrivKey(self):
        return self.privKey

    def setPubKey(self, pubKey):
        self.pubKey = pubKey

    def getPubKey(self):
        return self.pubKey
