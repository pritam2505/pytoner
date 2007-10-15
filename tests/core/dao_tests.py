
import unittest
from toner import core

class testDaoHeritageClass(core.Dao):
  def __init__(self):
    core.Dao.__init__(self)

class DaoTests(unittest.TestCase):
  def testDaoHeritage(self):
    """[Core][Dao] test heritage"""
    dao = testDaoHeritageClass()
    self.assertEqual(dao._logs, core.Logs())
    self.assertEqual(dao._sql, core.Sql())
    self.assertEqual(dao._config, core.Config())


