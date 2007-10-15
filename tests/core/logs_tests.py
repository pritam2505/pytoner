
import unittest
from toner import core 

class LogsTests(unittest.TestCase):
  def testLogsSingleton(self):
    """[Core][Logs] test singleton"""
    single1 = core.Logs()
    single2 = core.Logs()
    single3 = core.Logs()

    self.assertEqual(single1, single2)
    self.assertEqual(single2, single3)


