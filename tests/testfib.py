#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import fib


class TestFib(unittest.TestCase):

    def test_fib(self):
        # returns input place number in Fibonacci sequence.
        # If not a integer, return "Not a valid input!"
        eighth_place = fib.fib(8)
        first_place = fib.fib(1)
        string_input = fib.fib("Test")
        self.assertEquals(eighth_place, 13)
        self.assertEquals(first_place, 0)
        self.assertEquals(string_input, "Not a valid input!")


if __name__ == '__main__':
    unittest.main()
