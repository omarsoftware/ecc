import random as rand
from math import sqrt


class Point:
    def __init__(self, x=0, y=0, infinity=False):
        self.x = x
        self.y = y
        self.infinity = infinity

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def is_infinity(self):
        return self.infinity

    def print(self):
        str_print = ""
        if self.infinity:
            str_print = "punto en el infinito"
        else:
            str_print = "(" + str(self.x) + ", " + str(self.y) + ")"
        return str_print

    def __eq__(self, other_point):
        if other_point.is_infinity() and self.is_infinity():
            return True
        if (not other_point.is_infinity() and self.is_infinity()) or (
                other_point.is_infinity() and not self.is_infinity()):
            return False
        return self.get_x() == other_point.get_x() and self.get_y() == other_point.get_y()


class EllipticCurve:
    def __init__(self, a, b, q, g=None, n=None, h=None):

        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(q, int):
            raise AssertionError("a, b y q deben ser números")

        if not 0 <= a < q:
            raise AssertionError("a debe ser mayor o igual a 0 y menor a q")

        if not 0 <= b < q:
            raise AssertionError("b debe ser mayor o igual a 0 y menor a q")

        if not self.is_prime(q, 4):
            raise AssertionError("q debe ser un número primo")

        if not q > 2:
            raise AssertionError("q debe ser mayor a 2")

        if not self.is_non_singular(a, b, q):
            raise AssertionError("curva elíptica singular")

        self.a = a
        self.b = b
        self.q = q
        self.predefined = False
        self.infinity = Point(0, 0, True)
        if g:
            self.g = g
            self.n = n
            self.h = h
            self.predefined = True

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

    def is_predefined(self):
        return self.predefined

    def is_non_singular(self, a, b, q):
        if q:
            return (4 * (a ** 3) + 27 * (b ** 2)) % q != 0
        else:
            return (4 * (a ** 3) + 27 * (b ** 2)) != 0

    def belongs_to_curve(self, point):
        if not isinstance(point, Point):
            raise AssertionError("parámetro de tipo incorrecto")

        return (point.get_y() ** 2) % self.q == \
               ((point.get_x() ** 3) + self.a * point.get_x() + self.b) % self.q

    def get_points(self):
        left_side = []
        right_side = []
        points = []
        final_points = []

        for x in range(self.q):
            left_side.append((x, (x ** 2) % self.q))
            right_side.append((x, ((x ** 3) + (self.a * x) + self.b) % self.q))

        for val_l in left_side:
            for val_r in right_side:
                if val_l[1] == val_r[1]:
                    points.append((val_r[0], val_l[0]))

        points.sort(key=lambda y: y[0])

        for point in points:
            final_points.append(Point(point[0], point[1], False))

        return final_points

    def point_addition(self, point_p, point_q):

        if point_p.is_infinity() and point_q.is_infinity():
            return self.infinity

        if point_p.is_infinity() and not point_q.is_infinity():
            return point_q

        if point_q.is_infinity() and not point_p.is_infinity():
            return point_p

        if point_p.get_x() == point_q.get_x() and \
                (point_p.get_y() != point_q.get_y() or point_p.get_y() == 0):
            return self.infinity

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

    '''Calculates n * P by direct algorithm'''

    def direct_mult(self, point, k):
        point_r = self.infinity
        for x in range(k):
            point_r = self.point_addition(point_r, point)
        return point_r

    '''Calculates n * P by double-and-add algorithm'''

    def double_and_add(self, point, n):
        point_r = self.infinity
        while n > 0:
            if n & 1 == 1:
                point_r = self.point_addition(point_r, point)
            n, point = n >> 1, self.point_addition(point, point)
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
        s0, s1, t0, t1 = 1, 0, 0, 1
        while b > 0:
            q, r = divmod(a, b)
            a, b = b, r
            s0, s1, t0, t1 = s1, s0 - q * s1, t1, t0 - q * t1
            pass
        return s0, t0, a

    def inv(self, n, q):
        return self.egcd(n, q)[0] % q

    def power(self, x, y, p):
        res = 1
        x = x % p
        while y > 0:
            if y & 1:
                res = (res * x) % p
            y = y >> 1
            x = (x * x) % p
        return res

    def miillerTest(self, d, n):
        a = 2 + rand.randint(1, n - 4)
        x = self.power(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    def is_prime(self, n, k):
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True
        d = n - 1
        while d % 2 == 0:
            d //= 2
        for i in range(k):
            if not self.miillerTest(d, n):
                return False
        return True


class User:
    def __init__(self):
        self.priv_key = None
        self.pub_key = None

    def set_priv_key(self, priv_key):
        self.priv_key = priv_key

    def get_priv_key(self):
        return self.priv_key

    def set_pub_key(self, pub_key):
        self.pub_key = pub_key

    def get_pub_key(self):
        return self.pub_key


class ECDH:

    def __init__(self, elliptic_curve):
        self.ec = elliptic_curve

    def gen_priv(self, elliptic_curve):
        return rand.randint(1, elliptic_curve.get_n())

    def gen_pub_key(self, priv_key):
        if not 0 < priv_key:
            raise AssertionError("la clave privada debe ser mayor a 0")

        return self.ec.double_and_add(self.ec.get_g(), priv_key)

    def calc_shared_key(self, priv, pub):
        return self.ec.double_and_add(pub, priv)
