import numbers as num
import random as rand

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
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other_point):
        return self.get_x() == other_point.get_x() and self.get_y() == other_point.get_y()


class EllipticCurve:
    def __init__(self, a, b, q=None, g=None, n=None, h=None):

        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(q, int):
            raise AssertionError("a, b y q deben ser números")

        if not 0 <= a < q:
            raise AssertionError("a debe ser mayor o igual a 0 y menor a q")

        if not 0 <= b < q:
            raise AssertionError("b debe ser mayor o igual a 0 y menor a q")

        if not q > 2:
            raise AssertionError("q debe ser mayor a 2")

        if not self.isNonSingular(a, b, q):
            raise AssertionError("curva elíptica singular")

        self.a = a
        self.b = b
        self.q = q
        self.g = g
        self.n = n
        self.h = h
        self.zero = Point(0, 0)
        self.predefined = False

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

    def set_g(self, g):
        self.g = g

    def get_g(self):
        return self.g

    def set_n(self, n):
        self.n = n

    def get_n(self):
        return self.n

    def set_h(self, h):
        self.h = h

    def get_h(self):
        return self.h

    def isPreDefined(self):
        return self.predefined

    def setPreDefined(self, bool_val):
        self.predefined = bool_val

    def isNonSingular(self, a, b, q):
        if q:
            return (4 * (a ** 3) + 27 * (b ** 2)) % q != 0
        else:
            return (4 * (a ** 3) + 27 * (b ** 2)) != 0

    def belongsToCurve(self, point):
        if not isinstance(point, Point):
            raise AssertionError("parámetro de tipo incorrecto")

        return (point.get_y() ** 2) % self.q == \
               ((point.get_x() ** 3) + self.a * point.get_x() + self.b) % self.q

    def point_addition(self, point_p, point_q):
        if point_p.get_x() == 0 and point_p.get_y() == 0:
            return point_q

        if point_q.get_x() == 0 and point_q.get_y() == 0:
            return point_p

        if point_p.get_x() == point_q.get_x() and \
           (point_p.get_y() != point_q.get_y() or point_p.get_y() == 0):
            return self.zero

        if point_p.get_x() == point_q.get_x():
            slope = (3 * point_p.get_x() * point_p.get_x() + self.a) * \
                    self.inv(2 * point_p.get_y(), self.q) % self.q
            pass
        else:
            slope = (point_q.get_y() - point_p.get_y()) * \
                    self.inv(point_q.get_x() - point_p.get_x(), self.q) % self.q
            pass

        point_r = Point()

        x = (slope * slope - point_p.get_x() - point_q.get_x()) % self.q
        y = (slope * (point_p.get_x() - x) - point_p.get_y()) % self.q

        point_r.set_x(x)
        point_r.set_y(y)

        return point_r

    def point_doubling(self, point):
        alpha = (3 * point.get_x() ** 2 + self.get_a()) / (2 * point.get_y())

        point_r = Point()
        point_r.set_x(alpha ** 2 - 2 * point.get_x())
        point_r.set_y(alpha * (point.get_x() - point_r.get_x()) - point.get_y())

        return point_r

    def point_mult(self, point, k):
        '''
        point_r = self.zero
        for x in range(k):
            point_r = self.point_addition(point_r, point)

        return point_r
        '''
        point_r = self.zero
        m = point

        while k > 0:
            if k & 1 == 1:
                point_r = self.point_addition(point_r, m)
                pass
            k, m = k >> 1, self.point_addition(m, m)
            pass
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
            text += " " + str(self.b)

        if self.q:
            text += "(mod " + str(self.q) + ")"

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

    def sqrt(self, n, q):
        """sqrt on PN modulo: returns two numbers or exception if not exist
        >>> assert (sqrt(n, q)[0] ** 2) % q == n
        >>> assert (sqrt(n, q)[1] ** 2) % q == n
        """
        assert n < q
        for i in range(1, q):
            if i * i % q == n:
                return Point(i, q - i)
            pass
        raise Exception("not found")

    def at(self, x):
        """find points on curve at x
        - x: int < q
        - returns: ((x, y), (x,-y)) or not found exception
        >>> a, ma = ec.at(x)
        >>> assert a.x == ma.x and a.x == x
        >>> assert a.x == ma.x and a.x == x
        >>> assert ec.neg(a) == ma
        >>> assert ec.is_valid(a) and ec.is_valid(ma)
        """
        assert x < self.q
        ysq = (x ** 3 + self.a * x + self.b) % self.q
        y, my = self.sqrt(ysq, self.q)
        return Point(x, y), Point(x, my)

    def get_ec_parms(self, curve):
        pass


class User:
    def __init__(self):
        self.privKey = None
        self.pubKey = None

    def setPrivKey(self, privKey):
        self.privKey = privKey

    def getPrivKey(self):
        return self.privKey

    def setPubKey(self, pubKey):
        self.pubKey = pubKey

    def getPubKey(self):
        return self.pubKey


class ECDH:

    def __init__(self, elliptic_curve):
        self.ec = elliptic_curve

    def gen_priv(self, elliptic_curve):
        return rand.randint(1, elliptic_curve.get_n())

    def gen_pub_key(self, priv_key):
        if not 0 < priv_key < self.ec.get_n():
            raise AssertionError("la clave privada debe ser mayor a 0 y menor a n")

        return self.ec.point_mult(self.ec.get_g(), priv_key)

    def calc_shared_key(self, priv, pub):
        return self.ec.point_mult(pub, priv)


class ECDSA:

    def __init__(self, elliptic_curve):
        self.ec = elliptic_curve

    def sign(self, hashval, priv, r):
        m = self.ec.point_mult(self.ec.get_g(), r)
        p = Point(m.get_x(), self.inv(r, self.ec.get_n()) * (hashval + m.get_x() * priv) % self.ec.get_n())
        return p

    def verify(self):
        pass
