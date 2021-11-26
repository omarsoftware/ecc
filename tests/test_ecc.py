import unittest

import constants as cons
import ecmath as ec


class TestEllipticCurve(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
