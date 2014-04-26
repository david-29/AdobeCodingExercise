# Distinct Prime Factors

import math


def potential_primes():
    """Generator for primes < 30 and integers > 30 co-prime to 30"""

    s = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for ii in s:
        yield ii
    s = (1,) + s[3:]
    k = 30
    while True:
        for jj in s:
            yield jj + k
        k += 30


def get_factors(n):
    """Get the factors of a number as a list of tuples (factor, power)"""

    factors = []
    sqrt_n = math.sqrt(n)
    for divisor in potential_primes():
        if divisor > sqrt_n:
            break
        power = 0
        while (n % divisor) == 0:
            n //= divisor
            power += 1
        if power > 0:
            factors.append((divisor, power))
            sqrt_n = math.sqrt(n)
    if n > 1:
        factors.append((n, 1))
    return factors


def find_n_consecutive_numbers_with_n_distinct_prime_factors(n):
    """
    Find <n> consecutive numbers such that each has exactly <n>
    distinct prime factors
    """

    if n < 2:
        raise RuntimeError("n must be >= 2")
    x = 2
    while True:
        xf = get_factors(x)
        if len(xf) != n:
            x += 1
            continue
        n_found = 0
        for i in range(1, n):
            y = x + i
            yf = get_factors(y)
            if len(yf) != n:
                break
            n_found += 1
        if n_found < (n - 1):
            x += 1
            continue
        break
    return x
