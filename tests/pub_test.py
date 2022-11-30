import unittest
from src.pub import Pub
from src.drink import Drink
class TestPub(unittest.TestCase):

    def setUp(self):
        self.instance_of_pub = Pub("The flying bull", 200.00)
        self.instance_of_drink = Drink("Scotch Whisky", 10)
    

    def test_pub_has_name(self):
        self.assertEqual("The flying bull", self.instance_of_pub.name)

    def test_pub_has_till(self):
        self.assertEqual(200.00, self.instance_of_pub.till)

    def test_add_drink_to_menu(self):
        self.instance_of_pub.add_drink_to_menu(self.instance_of_drink)
        self.assertEqual(1, len(self.instance_of_pub.drinks))


