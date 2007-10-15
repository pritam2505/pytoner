
import unittest
from toner import dao, models

class BrandTests(unittest.TestCase):
  def setUp(self):
    try:
      self._brand_dao = dao.Brand()
    except:
      self.fail("Cannot construct models.Brand()")

    self._brand_name = "test_brand"

  def tearDown(self):
    self._brand_dao = None
    self._brand_name = None

  def add_brand_name(self):
    brand = models.Brand(brand_name=self._brand_name)
    self._brand_dao.add(brand)

  def del_brand_name(self):
    brand = self._brand_dao.del_by_name(self._brand_name)

  def testBrandAdd(self):
    """[Dao][Brand] add a Brand"""
    self.add_brand_name()

    brand = self._brand_dao.get_by_name(self._brand_name)
    self.assertNotEqual(brand, None)

    self.del_brand_name()

  def testBrandDelByName(self):
    """[Dao][Brand] del by name"""
    self.add_brand_name()
    brand = self._brand_dao.del_by_name(self._brand_name)
    brand = self._brand_dao.get_by_name(self._brand_name)
    self.assertEqual(brand, None)

  def testBrandDelById(self):
    """[Dao][Brand] del by id"""
    self.add_brand_name()
    brand = self._brand_dao.get_by_name(self._brand_name)
    self._brand_dao.del_by_id(brand._id)
    
    brand = self._brand_dao.get_by_name(self._brand_name)
    self.assertEqual(brand, None)

  def testBrandGetByName(self):
    """[Dao][Brand] get by name"""
    self.add_brand_name()

    brand = self._brand_dao.get_by_name(self._brand_name)
    self.assertNotEqual(brand, None)

    self.del_brand_name()

  def testBrandGetBtId(self):
    """[Dao][Brand] get by id"""
    self.add_brand_name()

    brand = self._brand_dao.get_by_name(self._brand_name)
    brand2 = self._brand_dao.get_by_id(brand._id)
    self.assertNotEqual(brand2, None)

    self.del_brand_name()

  def testBrandExistByName(self):
    """[Dao][Brand] exist by name"""
    self.add_brand_name()
    exist = self._brand_dao.exists_by_name(self._brand_name)
    self.assertEqual(exist, True)
    self.del_brand_name()
    exist = self._brand_dao.exists_by_name(self._brand_name)
    self.assertEqual(exist, False)

  def testBrandExistsById(self):
    """[Dao][Brand] exists by name"""
    self.add_brand_name()
    brand = self._brand_dao.get_by_name(self._brand_name)
    exist = self._brand_dao.exists_by_id(brand._id)
    self.assertEqual(exist, True)
    self.del_brand_name()
    exist = self._brand_dao.exists_by_id(brand._id)
    self.assertEqual(exist, False)

  def testBrandUpdate(self):
    """[Dao][Brand] update"""
    update_name="test_brand_update"
    self.add_brand_name()
    brand = self._brand_dao.get_by_name(self._brand_name)
    brand._name = update_name
    self._brand_dao.update(brand)

    brand = self._brand_dao.get_by_id(brand._id)
    self.assertEqual(brand._name, update_name)

    exist = self._brand_dao.exists_by_name(self._brand_name)
    self.assertEqual(exist, False)

    brand._name = self._brand_name
    self._brand_dao.update(brand)
    self.del_brand_name()
   
  def testBrandSearch(self):
    """[Dao][Brand] search"""
    self.add_brand_name()

    search1 = '%' + '%s' % (self._brand_name[2:7]) + '%'
    search2 = "you should not find me" 

    result = self._brand_dao.search(search1)
    self.assert_(len(result) >= 1)

    result = self._brand_dao.search(search2)
    self.assertEqual(len(result), 0)

    self.del_brand_name()

