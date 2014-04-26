#! /usr/bin/env python

import sys
import pandigitalPrimes


def main(argv):
    """
    Determine the largest prime pandigital number ...
      (a) overall -- use input '*'
      (b) of order <n> -- use input <n>
    """

    if len(argv) != 1:
        print('Usage:  runPandigitalPrimes {* | <num>}')
        return 1

    if argv[0] == '*':
        p_max = 0
        for ii in range(4, 10):
            for p_str in pandigitalPrimes.generate_pandigitals(ii):
                p = int(p_str)
                if pandigitalPrimes.is_prime(p):
                    if p > p_max:
                        p_max = p
            # print(' -- ii: {0},  p_max: {1}'.format(ii, p_max))
        if p_max > 0:
            print('\nThe largest prime pandigital number is: {0}'.format(p_max))

    else:
        nn = int(argv[0])
        p_max = pandigitalPrimes.find_largest_prime_pandigital_number(nn)
        if p_max > 0:
            print('\nThe largest prime pandigital number of order {0} is: {1}'.format(nn, p_max))
        else:
            print('\nNo prime pandigital numbers of order {0} found.'.format(nn))

    return 0


if __name__ == '__main__':
    rc = main(sys.argv[1:])
    sys.exit(rc)