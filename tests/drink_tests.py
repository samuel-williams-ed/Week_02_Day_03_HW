import unittest

from src.drinks import Drinks


class TestDrinks(unittest.TestCase):
    def setUp(self):
        test_drinks = [
        {"name":"jager", "price":2, "strength":10, "stock":25},
        {"name":"Tennents", "price":3, "strength":5, "stock":88},
        {"name":"Mystery Shot", "price":2, "strength":15, "stock":1}
        ]
        # test_drinks_01 = Drinks("Jager", 2, 10, 25)
        # test_drinks_02 = Drinks("Tennents", 3, 5, 88)
        # test_drinks_03 = Drinks("Mysetery Shot", 2, 15, 1)
