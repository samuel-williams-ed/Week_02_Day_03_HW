import unittest

from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food_test_burger = Food("Burger", 15, 25)
        self.food_test_chips = Food("Chips", 5, 12)

    def test_food_has_name(self):
        self.assertEqual("Burger", self.food_test_burger.name)

    def test_food_has_price(self):
        self.assertEqual(15, self.food_test_burger.price)

    def test_food_has_rejuvenation(self):
        self.assertEqual(25, self.food_test_burger.rejuvenation_level)



