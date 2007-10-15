
import unittest

import core
import models
import dao

test_suite_core = unittest.defaultTestLoader.loadTestsFromModule(core)
test_suite_models = unittest.defaultTestLoader.loadTestsFromModule(models)
test_suite_dao = unittest.defaultTestLoader.loadTestsFromModule(dao)


test_suite = unittest.TestSuite()
test_suite.addTests(test_suite_core)
test_suite.addTests(test_suite_models)
test_suite.addTests(test_suite_dao)

