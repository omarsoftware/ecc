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

    def test_predifined_curve_1(self):
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

    def test_predefined_curve_2(self):
        curva = cons.EC_LIST["brainpoolP192r1"]
        elliptic_curve = ec.EllipticCurve(curva["a"], curva["b"], curva["q"], curva["g"], curva["n"], curva["h"])
        ecdh = ec.ECDH(elliptic_curve)
        bob_priv_key = 0x378394C3274253FD15531812
        bob_pub_key = ecdh.gen_pub_key(bob_priv_key)

        alice_priv_key = 0x151FF34164E0A753BAE0B506
        alice_pub_key = ecdh.gen_pub_key(alice_priv_key)

        shared_secret_by_bob = ecdh.calc_shared_key(bob_priv_key, alice_pub_key)
        shared_secret_by_alice = ecdh.calc_shared_key(alice_priv_key, bob_pub_key)

        # expected point as result:
        point_r = ec.Point(4239331162207121876592347022408768142110490207776903487994,
                           2633299400031971237830977525947079928403296132141738036252)

        self.assertEqual(shared_secret_by_bob, shared_secret_by_alice)
        self.assertEqual(shared_secret_by_bob, point_r)
