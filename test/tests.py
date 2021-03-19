import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from foobar import bar, foo


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bar = bar.Bar('qux')

    def test1(self):
        self.assertEqual(self.bar.foo(), 'qux_foo')

    def test2(self):
        self.assertEqual(self.bar.bar(), 'qux_bar')


if __name__ == '__main__':
    unittest.main()
