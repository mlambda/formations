import unittest


def add(a, b):
    return a + b


class AddTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.integers = [(1, 2), (20, 22)]

    def test_commutativity(self):
        for a, b in self.integers:
            self.assertEqual(add(a, b), add(b, a))

    def test_associativity(self):
        for a, b in self.integers:
            self.assertEqual(add(add(a, b), b), add(a, add(b, b)))
