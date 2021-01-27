import unittest
from IIPE.script_test import hello

class TestHistory(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), 'Hello')
