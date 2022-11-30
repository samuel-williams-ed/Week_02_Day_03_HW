import unittest

from src.customers import Customers

class TestCustomers(unittest.TestCase):
    def setUp(self):
        self.customer_example = Customers("Peter", 27, 2, 400)

    def test_customer_has_name(self):
        self.assertEqual("Peter", self.customer_example.name)