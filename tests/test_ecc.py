import unittest
import constants as cons
import ecmath as ec
from ddt import ddt, data

@ddt
class TestEllipticCurve(unittest.TestCase):

    @data(("3", "4", "5"), (3.3, 4.4, 5.5), ("hola", "como", "estas"), ("", "", ""))
    def test_domain_params_are_int(self, value):
        with self.assertRaises(AssertionError) as context:
            elliptic_curve = ec.EllipticCurve(*value)
        self.assertTrue("a, b y q deben ser números" in str(context.exception))

    @data((-5, 15, 23), (0, 15, 23), (23, 15, 23), (24, 15, 23))
    def test_domain_a_range(self, value):
        with self.assertRaises(AssertionError) as context:
            elliptic_curve = ec.EllipticCurve(*value)
        self.assertTrue("a debe ser mayor a 0 y menor a q" in str(context.exception))

    @data((10, -15, 23), (10, 0, 23), (10, 23, 23), (10, 50, 23))
    def test_domain_b_range(self, value):
        with self.assertRaises(AssertionError) as context:
            elliptic_curve = ec.EllipticCurve(*value)
        self.assertTrue("b debe ser mayor a 0 y menor a q" in str(context.exception))

    @data((1, 1, 2))
    def test_domain_q_range(self, value):
        with self.assertRaises(AssertionError) as context:
            elliptic_curve = ec.EllipticCurve(*value)
        self.assertTrue("q debe ser mayor a 2" in str(context.exception))

    @data((2, 3, 5))
    def test_curve_non_singularity(self, value):
        with self.assertRaises(AssertionError) as context:
            elliptic_curve = ec.EllipticCurve(*value)
        self.assertTrue("curva elíptica singular" in str(context.exception))

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
        self.elliptic_curve = ec.EllipticCurve(curva["a"], curva["b"], curva["q"], ec.Point(curva["g"][0],
                                               curva["g"][1]), curva["n"], curva["h"])
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
        self.elliptic_curve = ec.EllipticCurve(curva["a"], curva["b"], curva["q"], ec.Point(curva["g"][0],
                                               curva["g"][1]), curva["n"], curva["h"])
        ecdh = ec.ECDH(self.elliptic_curve)
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


class TestECDSA(unittest.TestCase):

    def test_sign_1(self):
        '''
        elliptic_curve = ec.EllipticCurve(1, 18, 19)
        g = elliptic_curve.at(7)

        dsa = ec.DSA(elliptic_curve, g)

        priv = 6
        pub = ec.Point(1, 16)
        hashval = 128
        r = 7

        # sig = dsa.sign(hashval, priv, r)
        # assert dsa.validate(hashval, sig, pub)
        '''
        pass

