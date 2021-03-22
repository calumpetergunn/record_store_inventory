import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Castlemania", "Thee Oh Sees", "Castleface Records", "LP", "Psychedelic", 25, 9.50, 15.99)

    def test_product_has_title(self):
        self.assertEqual("Castlemania", self.product.title)

    def test_product_has_artist(self):
        self.assertEqual("Thee Oh Sees", self.product.artist)

    def test_product_has_record_label(self):
        self.assertEqual("Castleface Records", self.product.record_label)

    def test_product_has_format(self):
        self.assertEqual("LP", self.product.format)
        
    def test_product_has_genre(self):
        self.assertEqual("Psychedelic", self.product.genre)
        
    def test_product_has_quantity(self):
        self.assertEqual(25, self.product.quantity)
        
    def test_product_has_buy_cost(self):
        self.assertEqual(9.50, self.product.buy_cost)
        
    def test_product_has_sell_price(self):
        self.assertEqual(15.99, self.product.sell_price)

    def can_add_stock(self):
        self.product.add_stock(30)
        self.assertEqual(55, self.product.quantity)




