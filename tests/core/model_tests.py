
import unittest
from toner import core

class testModelHeritageClass(core.Model):
  def __init__(self):
    core.Model.__init__(self)

class ModelTests(unittest.TestCase):
  def testModelHeritage(self):
    """[Core][Model] test heritage"""
    model = testModelHeritageClass()
    self.assertEqual(model._logs, core.Logs())
    self.assertEqual(model._sql, core.Sql())
    self.assertEqual(model._config, core.Config())


