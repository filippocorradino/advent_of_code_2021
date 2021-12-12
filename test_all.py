#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2021 - Tests

Simple test script, nothing fancy
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from importlib import import_module
import unittest


class TestResults(unittest.TestCase):

    solutions = {'day06': [394994, 1765974267455]}

    def test_results(self):
        """
        Test all challenges scripts results
        """
        for script in self.solutions:
            print("Testing {0}.py...".format(script))
            with self.subTest(i=script):
                module = import_module(script)
                self.assertEqual(module.main(), self.solutions[script])
        print("All done")


if __name__ == '__main__':
    unittest.main()
