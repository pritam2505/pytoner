
import unittest
from toner import dao, models

class ProductTests(unittest.TestCase):
  def setUp(self):
    try:
      self._product_dao = dao.Product()
    except:
      self.fail("Constructor raise exception.")

    self._brand_dao = dao.Brand()
    self._brand_name = "product_test"
    self._product_name = "product_test"

  def tearDown(self):
    self._brand_dao = None
    self._brand_name = None
    self._product_dao = None
    self._product_name = None

  def add_a_product(self):
    brand = models.Brand(brand_name=self._brand_name)
    self._brand_dao.add(brand)
    self._brand = self._brand_dao.get_by_name(self._brand_name)
    product = models.Product(brand=self._brand, product_name=self._product_name)
    self._product_dao.add(product)

  def del_a_product(self):
    self._product_dao.del_by_name(self._product_name)
    self._brand_dao.del_by_name(self._brand_name)
    

  def testProductAdd(self):
    """[Dao][Product] add"""
    self.add_a_product()
    product = self._product_dao.get_by_name(self._product_name)
    self.assertNotEqual(product, None)
    self.del_a_product()

  def testProductDelByName(self):
    """[Dao][Product] del by name"""
    self.add_a_product()
    self._product_dao.del_by_name(self._product_name)
    self._brand_dao.del_by_name(self._brand_name)

    product = self._product_dao.get_by_name(self._product_name)
    self.assertEqual(product, None)

  def testProductDelById(self):
    """[Dao][Product] del by id"""
    self.add_a_product()
    product = self._product_dao.get_by_name(self._product_name)
    self._product_dao.del_by_id(product._id)
    self._brand_dao.del_by_name(self._brand_name)

    product = self._product_dao.get_by_name(self._product_name)
    self.assertEqual(product, None)

  def testProductGetByName(self):
    """[Dao][Product] get by name"""
    self.add_a_product()
    product = self._product_dao.get_by_name(self._product_name)
    self.assertNotEqual(product, None)

    self.del_a_product()
    product = self._product_dao.get_by_name(self._product_name)
    self.assertEqual(product, None)

  def testProductGetById(self):
    """[Dao][Product] get by id"""
    self.add_a_product()
    product1 = self._product_dao.get_by_name(self._product_name)
    product2 = self._product_dao.get_by_id(product1._id)
    self.assertNotEqual(product2, None)
    self.assertEqual(product1._id, product2._id)
    self.del_a_product()

  def testProductUpdate(self):
    """[Dao][Product] update"""
    self.add_a_product()
    update_name="product_update"
    product = self._product_dao.get_by_name(self._product_name)
    product._name = update_name
    self._product_dao.update(product)

    product2 = self._product_dao.get_by_id(product._id)
    self.assertNotEqual(product2, None)
    self.assertEqual(product._name, product2._name)
 
    product2 = self._product_dao.get_by_name(self._product_name)
    self.assertEqual(product2, None)

    product._name = self._product_name
    self._product_dao.update(product)
    self.del_a_product()
