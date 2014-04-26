#! /usr/bin/env python

import sys
import distinctPrimeFactors


def main(argv):
    """
    Find <n> consecutive numbers each with exactly <n> distinct prime factors
    """

    if len(argv) != 1:
        print('Usage:  runDistinctPrimeFactors <num>')
        return 1

    nn = int(argv[0])

    first = distinctPrimeFactors.find_n_consecutive_numbers_with_n_distinct_prime_factors(nn)

    print('\nFor n: {0}, first of {0} consecutive numbers with {0} distinct prime factors is: {1}'.format(nn, first))

    return 0


if __name__ == '__main__':
    rc = main(sys.argv[1:])
    sys.exit(rc)