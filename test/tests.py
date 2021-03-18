import unittest
from app import app


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.App('qux')

    def test1(self):
        self.assertEqual(self.app.foo(), 'qux_foo')

    def test2(self):
        self.assertEqual(self.app.bar(), 'qux_bar')


if __name__ == '__main__':
    unittest.main()