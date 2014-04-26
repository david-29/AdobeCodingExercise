# Find the Largest Prime Pandigital Numbers

import math

from itertools import *


def generate_pandigitals(n):
    """Generate all 1-to-<n> pandigitals"""

    return (''.join(x) for x in list(permutations('123456789'[:n])))


def is_prime(n):
    """Determine if a given number is a prime"""

    rv = False
    ub = math.ceil(math.sqrt(n)) + 1
    for div in range(2, ub):
        if n % div == 0:
            break
    else:
        rv = True
    return rv


def find_largest_prime_pandigital_number(n):
    """Find the largest prime pandigital number of order <n>"""

    p_max = 0
    for p_str in generate_pandigitals(n):
        p = int(p_str)
        if is_prime(p):
            if p > p_max:
                p_max = p
    return p_max
