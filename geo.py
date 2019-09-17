#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple geometric numbers sequence function"""

__author__ = "astephens91"


def square(num):
    """Squares input"""
    if isinstance(num, (int, long)):
        return (num * num)
    else:
        return "Not a valid input!"


def triangle(num):
    """Creates triangular number from input"""
    if isinstance(num, (int, long)):
        return (num * (num + 1) / 2)
    else:
        return "Not a valid input!"


def cube(num):
    """Cubes input"""
    if isinstance(num, (int, long)):
        return num**3
    else:
        return "Not a valid input!"


def main():
    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))


if __name__ == "__main__":
    main()
