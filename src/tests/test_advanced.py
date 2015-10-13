# -*- coding: utf-8 -*-

from .context import my_module

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        my_module.core.hello()


if __name__ == '__main__':
    unittest.main()
