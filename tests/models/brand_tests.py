
import unittest
from toner import models

class BrandTests(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testBrandConstruct(self):
    """[Models][Brand] Construct"""
    try:
      brand = models.Brand()
    except:
      self.fail("Cannot construct models.Brand()")

  def testBrandConstructWithStringInBrandId(self):
    """[Models][Brand] Construct with string in brand_id"""
    try:
      brand = models.Brand(brand_id="string")
      self.fail("Construct should raise TypeError")
    except:
      pass

  def testBrandContstructValues(self):
    """[Models][Brand] Verif default value"""
    brand = models.Brand()
    self.assertEqual(brand._id, -1)
    self.assertEqual(brand._name, "")

  def testBrandConstructWithParams(self):
    """[Models][Brand] Verif value set in params"""
    brand = models.Brand(brand_id=1, brand_name="Hello")
    self.assertEqual(brand._id, 1)
    self.assertEqual(brand._name, "Hello")

