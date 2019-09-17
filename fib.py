#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple fibonacci sequence function"""

__author__ = "astephens91"


def fib(n):
    if isinstance(n, (int, long)):
        a, b = (0, 1)
        for _ in range(n-1):
            a, b = b, a + b
        return a
    else:
        return "Not a valid input!"


def main():
    print ("Fibonacci")
    for i in range(10):
        print ("{}: {}".format(i, fib(i)))


if __name__ == "__main__":
    main()
