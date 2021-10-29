import unittest
import startPage

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(startPage.test01(), 5)

unittest.main()