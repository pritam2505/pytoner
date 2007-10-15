
import unittest
from toner import models

class ProductTests(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testProductConstruct(self):
    """[Models][Product] construct"""
    try:
      product = models.Product()
    except:
      self.fail("Constructor raise exception.")

  def testProductConstructWithStringInProductId(self):
    """[Models][Product] construct with a string in product_id"""
    try:
      product = models.Product(product_id="Hello")
      self.fail("should raise TypeError exception")
    except:
      pass

  def testProductConstructWithStringInProductCount(self):
    """[Models][Product] construct with a string in product_count"""
    try:
      product = models.Product(product_count="Hello")
      self.fail("should raise TypeError exception")
    except:
      pass

  def testProductConstructDefaultValue(self):
    """[Models][Product] check default construct values"""
    product = models.Product()
    self.assertEqual(product._id, -1)
    self.assertEqual(product._brand._id, -1)
    self.assertEqual(product._brand._name, "")
    self.assertEqual(product._name, "")
    self.assertEqual(product._desc, "")
    self.assertEqual(product._count, 0)

  def testProductConstructWithValue(self):
    """[Models][Product] check construct with args values"""
    brand = models.Brand(brand_id=1, brand_name="brand_name")
    product = models.Product(product_id=2, brand=brand, product_name="name", product_desc="desc", product_count=3)
    self.assertEqual(product._id, 2)
    self.assertEqual(product._brand._id, 1)
    self.assertEqual(product._brand._name, "brand_name")
    self.assertEqual(product._name, "name")
    self.assertEqual(product._desc, "desc")
    self.assertEqual(product._count, 3)

