import unittest

from src.pub import Pub
from src.drinks import Drinks
from src.customers import Customers

class TestPub(unittest.TestCase):
    def setUp(self):  
        self.test_drinks =[
        {"name":"jager", "price":2, "strength":10, "stock":25},
        # {"name":"Tennents", "price":3, "strength":5, "stock":88},
        # {"name":"Mystery Shot", "price":2, "strength":15, "stock":1}
        ]
        self.test_pub = Pub("Merrygold", 1000)
        self.stock_the_bar = self.test_pub.add_drinks_to_stock(self.test_drinks)
        #customer ( name, age, drnukness, cash)
        self.test_customer = Customers("Jeremy", 27, 0, 25)

    def test_pubs_has_drinks(self):
        self.assertEqual(1, self.test_pub.get_drinks_list_length())

    def test_pub_gained_money(self):
        self.test_pub.sell_drink(self.test_customer, self.test_drinks)
        self.assertEqual(1002, self.test_pub.till)
        
    def test_pub_check_age(self):
        self.assertEqual(True, self.test_pub.check_age(self.test_customer))

    def test_customer_gets_more_drunk(self):
        self.test_pub.sell_drink(self.test_customer, self.test_drinks)
        self.assertEqual(10, self.test_customer.drunkenness)
    
    def test_check_steamin(self):
        self.assertEqual(False, self.test_pub.check_steamin(self.test_customer))