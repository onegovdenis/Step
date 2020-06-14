import unittest
from features import *


class TestPin(unittest.TestCase):
    def setUp(self):
       self.my_atm = Atm()


    def test_money(self):
        self.assertTrue(self.my_atm.rise_money(1000))


    def test_pin(self):
        pin = my_atm.enter_pin(777)
        self.assertTrue(pin)


