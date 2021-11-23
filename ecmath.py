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
        return "("+str(self.x)+", "+str(self.y)+")"


class EllipticCurve:
    def __init__(self, a, b, q=None):
        self.a = a
        self.b = b
        self.q = q
        self.zero = Point(0, 0)

    def set_a(self, a):
        self.a = a

    def get_a(self):
        return self.a

    def set_b(self, b):
        self.b = b

    def get_b(self):
        return self.b

    def set_q(self, q):
        self.q = q

    def get_q(self):
        return self.q

    def isNonSingular(self):
        if self.q:
            return (4*(self.a**3)+27*(self.b**2)) % self.q != 0
        else:
            return (4*(self.a**3)+27*(self.b**2)) != 0


    def belongsToCurve(self, point):
        return (point.get_y()**2) % self.q == ((point.get_x()**3)+self.a*point.get_x()+self.b) % self.q

    def point_addition(self, point_p, point_q):
        '''
        alpha = (point_q.get_y() - point_p.get_y())/(point_q.get_x() - point_p.get_x())

        point_r = Point()
        point_r.set_x(alpha**2 - point_p.get_x() - point_q.get_x())
        point_r.set_y(alpha*(point_r.get_x() - point_p.get_x()) + point_p.get_y())

        point_pq = Point()
        point_pq.set_x(alpha**2 - point_p.get_x() - point_q.get_x())
        point_pq.set_y(alpha*(point_p.get_x() - point_r.get_x()) - point_p.get_y())
        '''

        if point_p.get_x() == 0 and point_p.get_y() == 0:
            return point_q

        if point_q.get_x() == 0 and point_q.get_y() == 0:
            return point_p

        if point_p.get_x() == point_q.get_x() and (point_p.get_y() != point_q.get_y() or point_p.get_y() == 0):
            return self.zero

        if point_p.get_x() == point_q.get_x():
            slope = (3 * point_p.get_x() * point_p.get_x() + self.a) * self.inv(2 * point_p.get_y(), self.q) % self.q
            pass
        else:
            slope = (point_q.get_y() - point_p.get_y()) * self.inv(point_q.get_x() - point_p.get_x(), self.q) % self.q
            pass

        point_r = Point()

        x = (slope * slope - point_p.get_x() - point_q.get_x()) % self.q
        # y = (point_p.get_y() + slope * (x - point_p.get_x())) % self.q
        y = (slope * (point_p.get_x() - x) - point_p.get_y()) % self.q

        point_r.set_x(x)
        point_r.set_y(y)

        return point_r

    def point_doubling(self, point):
        alpha = (3 * point.get_x() ** 2 + self.get_a()) / (2 * point.get_y())

        point_r = Point()
        point_r.set_x(alpha ** 2 - 2 * point.get_x())
        point_r.set_y(alpha*(point.get_x() - point_r.get_x()) - point.get_y())

        return point_r

    def point_mult(self, point, k):
        '''
        point_r = self.point_doubling(point)
        for x in range(k-2):
            point_r = self.point_addition(point, point_r)

        return point_r
        '''
        point_r = self.zero
        for x in range(k):
            point_r = self.point_addition(point_r, point)

        return point_r


    def print(self):
        text = "y\u00B2 = x\u00B3"
        if self.a > 0:
            text += " + " + str(self.a) + "x"
        elif self.a < 0:
            text += " " + str(self.a) + "x"

        if self.b > 0:
            text += " + " + str(self.b)
        elif self.b < 0:
            text += " "+str(self.b)

        if self.q:
            text += "(mod "+str(self.q)+")"

        return text

    def egcd(self, a, b):
        """extended GCD
        returns: (s, t, gcd) as a*s + b*t == gcd
        #>>> s, t, gcd = egcd(a, b)
        #>>> assert a % gcd == 0 and b % gcd == 0
        #>>> assert a * s + b * t == gcd
        """
        s0, s1, t0, t1 = 1, 0, 0, 1
        while b > 0:
            q, r = divmod(a, b)
            a, b = b, r
            s0, s1, t0, t1 = s1, s0 - q * s1, t1, t0 - q * t1
            pass
        return s0, t0, a

    def inv(self, n, q):
        """div on PN modulo a/b mod q as a * inv(b, q) mod q
        # >>> assert n * inv(n, q) % q == 1
        """
        # n*inv % q = 1 => n*inv = q*m + 1 => n*inv + q*-m = 1
        # => egcd(n, q) = (inv, -m, 1) => inv = egcd(n, q)[0] (mod q)
        return self.egcd(n, q)[0] % q
        # [ref] naive implementation
        # for i in range(q):
        #    if (n * i) % q == 1:
        #        return i
        #    pass
        # assert False, "unreached"
        # pass


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
