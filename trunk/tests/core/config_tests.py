
import unittest
from toner import core 

class ConfigTests(unittest.TestCase):
  def testConfigSingleton(self):
    """[Core][Config] test singleton"""
    single1 = core.Config()
    single2 = core.Config()
    single3 = core.Config()

    self.assertEqual(single1, single2)
    self.assertEqual(single2, single3)


