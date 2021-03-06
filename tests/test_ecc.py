import unittest
import constants as cons
from ecmath import ecmath as ec
from ddt import ddt, data

@ddt
class TestEllipticCurve(unittest.TestCase):

    @data(("3", "4", "5"), (3.3, 4.4, 5.5), ("hola", "como", "estas"), ("", "", ""))
    def test_domain_params_are_int(self, value):
        with self.assertRaises(AssertionError) as context:
            elliptic_curve = ec.EllipticCurve(*value)
        self.assertTrue("a, b y q deben ser números" in str(context.exception))

    @data((10, 15, 24))
    def test_domain_q_is_prime(self, value):
        with self.assertRaises(AssertionError) as context:
            elliptic_curve = ec.EllipticCurve(*value)
        self.assertTrue("q debe ser un número primo" in str(context.exception))


    @data((-5, 15, 23), (23, 15, 23), (24, 15, 23))
    def test_domain_a_range(self, value):
        with self.assertRaises(AssertionError) as context:
            elliptic_curve = ec.EllipticCurve(*value)
        self.assertTrue("a debe ser mayor o igual a 0 y menor a q" in str(context.exception))

    @data((10, -15, 23), (10, 23, 23), (10, 50, 23))
    def test_domain_b_range(self, value):
        with self.assertRaises(AssertionError) as context:
            elliptic_curve = ec.EllipticCurve(*value)
        self.assertTrue("b debe ser mayor o igual a 0 y menor a q" in str(context.exception))

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

    @data(([1, 6, 11], [(2, 4), (2, 7), (3, 5), (3, 6), (5, 2), (5, 9), (7, 2), (7, 9), (8, 3), (8, 8), (10, 2), (10, 9)]),
          ([10, 15, 23], [(1, 7), (1, 16), (3, 7), (3, 16), (4, 2), (4, 21), (5, 11), (5, 12), (8, 3), (8, 20), (9, 11), (9, 12), (12, 0), (14, 1), (14, 22), (16, 4), (16, 19), (18, 1), (18, 22), (19, 7), (19, 16), (20, 2), (20, 21), (22, 2), (22, 21)]))
    def test_points_over_curve(self, value):
        final_points = []
        curve = ec.EllipticCurve(*value[0])
        points = curve.get_points()
        for point in points:
            final_points.append((point.get_x(), point.get_y()))

        self.assertEqual(final_points, value[1])

    @data(([10, 15, 23], [3, 7, False], [9, 11, False], [14, 1, False]),
          ([10, 15, 23], [9, 11, False], [9, 12, False], [0, 0, True]),
          ([10, 15, 23], [3, 7, False], [3, 7, False], [18, 1, False]),
          ([10, 15, 23], [5, 12, False], [0, 0, True], [5, 12, False]),
          ([10, 15, 23], [0, 0, True], [5, 12, False], [5, 12, False]),
          ([10, 15, 23], [0, 0, True], [0, 0, True], [0, 0, True])
          )
    def test_addition(self, value):
        curve = ec.EllipticCurve(*value[0])
        point_p = ec.Point(*value[1])
        point_q = ec.Point(*value[2])
        point_r1 = ec.Point(*value[3])
        point_r2 = curve.point_addition(point_p, point_q)
        self.assertEqual(point_r1, point_r2)

    @data(([10, 15, 23], [8, 20], [9, 11]),
          ([10, 15, 23], [8, 20], [8, 20]),
          ([10, 15, 23], [8, 20], [0, 0, True]),
          ([10, 15, 23], [0, 0, True], [0, 0, True])
          )
    def test_commutativity(self, value):
        curve = ec.EllipticCurve(*value[0])
        point_p = ec.Point(*value[1])
        point_q = ec.Point(*value[2])
        point_p_plus_q = curve.point_addition(point_p, point_q)
        point_q_plus_p = curve.point_addition(point_q, point_p)
        self.assertEqual(point_p_plus_q, point_q_plus_p)

    @data(([10, 15, 23], (9, 11), 1, (9, 11)),
          ([10, 15, 23], (9, 11), 14, (18, 22)),
          ([10, 15, 23], (9, 11), 26, [0, 0, True]))
    def test_direct_multiplication(self, value):
        curve = ec.EllipticCurve(*value[0])
        point_p = ec.Point(*value[1])
        n = value[2]
        point_r = curve.direct_mult(point_p, n)
        point_f = ec.Point(*value[3])

        self.assertEqual(point_r, point_f)

    @data(([10, 15, 23], (9, 11), 1, (9, 11)),
          ([10, 15, 23], (9, 11), 14, (18, 22)),
          ([10, 15, 23], (9, 11), 26, [0, 0, True]))
    def test_double_and_add(self, value):
        curve = ec.EllipticCurve(*value[0])
        point_p = ec.Point(*value[1])
        n = value[2]
        point_r = curve.double_and_add(point_p, n)
        point_f = ec.Point(*value[3])

        self.assertEqual(point_r, point_f)


class TestECDH(unittest.TestCase):
    def test_predefined_curve_1(self):
        curva = cons.EC_LIST["brainpoolP192r1"]
        self.elliptic_curve = ec.EllipticCurve(curva["a"], curva["b"], curva["q"], ec.Point(curva["g"][0],
                                               curva["g"][1]), curva["n"], curva["h"])
        self.bob = ec.User()
        self.alice = ec.User()

        self.bob.set_priv_key(0x6)
        self.bob.set_pub_key(self.elliptic_curve.double_and_add(self.elliptic_curve.get_g(), self.bob.get_priv_key()))

        self.alice.set_priv_key(0x8)
        self.alice.set_pub_key(self.elliptic_curve.double_and_add(self.elliptic_curve.get_g(), self.alice.get_priv_key()))

        shared_secret_by_bob = self.elliptic_curve.double_and_add(self.alice.get_pub_key(), self.bob.get_priv_key())
        shared_secret_by_alice = self.elliptic_curve.double_and_add(self.bob.get_pub_key(), self.alice.get_priv_key())

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