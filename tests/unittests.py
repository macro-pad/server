import unittest
import testcode

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(testcode.test01(), 5)

unittest.main()