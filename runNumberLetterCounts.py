#! /usr/bin/env python

import sys
import numberLetterCounts


def main(argv):
    """
    Determine the number of letters used in spelling out the
    names of the numbers from num1 through num2
    """

    if len(argv) != 2:
        print('Usage:  runNumberLetterCounts <num1> <num2>')
        return 1

    n1 = int(argv[0])
    n2 = int(argv[1])

    count = numberLetterCounts.get_number_letter_count_for_range(n1, n2)

    print('\nRange:  [{0},{1}]   letter count:  {2}'.format(n1, n2, count))

    return 0


if __name__ == '__main__':
    rc = main(sys.argv[1:])
    sys.exit(rc)