
import unittest
from toner import core 

class SqlTests(unittest.TestCase):
  def testSqlSingleton(self):
    """[Core][Sql] test singleton"""
    single1 = core.Sql()
    single2 = core.Sql()
    single3 = core.Sql()

    self.assertEqual(single1, single2)
    self.assertEqual(single2, single3)


