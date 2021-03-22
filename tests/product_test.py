import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Castlemania", "Thee Oh Sees", "Castleface Records", "LP", "Psychedelic", 25, 9.50, 15.99)

    def test_product_has_name(self):
        self.assertEqual("Castelmania", self.product.name)