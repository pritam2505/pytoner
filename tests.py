#!/usr/bin/env python

import unittest
from toner import *
from tests import test_suite

unittest.TextTestRunner(verbosity=2).run(test_suite)

