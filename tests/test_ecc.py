import unittest
import constants as cons
import ecmath as ec


class TestEllipticCurve(unittest.TestCase):

    def test_addition(self):
        curve = ec.EllipticCurve(10, 15, 23)
        point_p = ec.Point(3, 7)
        point_q = ec.Point(9, 11)
        point_r1 = ec.Point(14, 1)
        point_r2 = curve.point_addition(point_p, point_q)
        self.assertEqual(point_r1, point_r2)

    def test_multiplication(self):
        curve = ec.EllipticCurve(10, 15, 23)
        point_p = ec.Point(3, 7)
        point_r = curve.point_mult(point_p, 19)
        point_f = ec.Point(22, 2)
        self.assertEqual(point_r, point_f)


class TestECDH(unittest.TestCase):

    def test_sarasa(self):
        curva = cons.EC_LIST["brainpoolP192r1"]
        self.elliptic_curve = ec.EllipticCurve(curva["a"], curva["b"], curva["q"], curva["g"], curva["n"], curva["h"])
        self.bob = ec.User()
        self.alice = ec.User()

        self.bob.setPrivKey(0x6)
        self.bob.setPubKey(self.elliptic_curve.point_mult(self.elliptic_curve.get_g(), self.bob.getPrivKey()))

        self.alice.setPrivKey(0x8)
        self.alice.setPubKey(self.elliptic_curve.point_mult(self.elliptic_curve.get_g(), self.alice.getPrivKey()))

        shared_secret_by_bob = self.elliptic_curve.point_mult(self.alice.getPubKey(), self.bob.getPrivKey())
        shared_secret_by_alice = self.elliptic_curve.point_mult(self.bob.getPubKey(), self.alice.getPrivKey())

        self.assertEqual(shared_secret_by_bob, shared_secret_by_alice)



