#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for "sheetmusic" in c-major-transposition
"""

import unittest

# This is a temporary import in order to test the structure of the project
from cmajortransposition.sheetmusic import test1

# This is a temporary class in order to test the structure of the project
class TestTest1(unittest.TestCase):
    def test_test1(self):
        self.assertEqual("test",test1())
