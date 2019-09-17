#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function that returns a list of prime numbers smaller than input
 and another that returns boolean if inputted number is prime"""

__author__ = "astephens91"

from math import sqrt


def primes(n):
    """Creates list of all prime number lower than n
        (based of the Sieve of Eratosthenes.)"""
    if isinstance(n, (int, long)):
        a = range(2, n + 1)
        b, c = [], a
        while c[0] < sqrt(n):
            starting_integer = c[0]
            b += [starting_integer]
            c = [x for x in c if x % starting_integer != 0]
        return b + c
    else:
        return "Not a valid input!"


def is_prime(n):
    if isinstance(n, (int, long)):
        if n >= 2:
            for x in range(2, n):
                if not (n % x):
                    return False
        else:
            return False
        return True
    else:
        return "Not a valid input!"


def main():
    print ("Primes")
    prime_list = primes(1000)
    for p in prime_list[-10:]:
        print (p)
    print ("Is 999981 prime? {}".format(is_prime(999981)))
    print ("Is 999983 prime? {}".format(is_prime(999983)))


if __name__ == "__main__":
    main()
